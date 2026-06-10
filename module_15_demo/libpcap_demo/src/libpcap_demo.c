#include <pcap/pcap.h>
#include <pcap/sll.h>

#include <arpa/inet.h>
#include <net/ethernet.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int g_datalink_type = 0;
static int g_seen_packets = 0;
static int g_tcp_packets = 0;

static pcap_t *open_capture_handle(const char *interface_name, char *errbuf) {
    return pcap_open_live(interface_name, BUFSIZ, 1, 1000, errbuf);
}

static int is_tcp_packet(const struct ip *ip_header) {
    return ip_header->ip_p == IPPROTO_TCP;
}

static int get_network_offset_and_protocol(
    const struct pcap_pkthdr *packet_header,
    const u_char *packet_bytes,
    size_t *network_offset,
    uint16_t *ether_type) 
{
    const struct ether_header *ether_header;
    const struct sll_header *linux_header;

    if (g_datalink_type == DLT_EN10MB) {
        if (packet_header->caplen < sizeof(struct ether_header)) {
            return 0;
        }

        ether_header = (const struct ether_header *)packet_bytes;
        *network_offset = sizeof(struct ether_header);
        *ether_type = ntohs(ether_header->ether_type);
        return 1;
    }

    if (g_datalink_type == DLT_LINUX_SLL) {
        if (packet_header->caplen < sizeof(struct sll_header)) {
            return 0;
        }

        linux_header = (const struct sll_header *)packet_bytes;
        *network_offset = sizeof(struct sll_header);
        *ether_type = ntohs(linux_header->sll_protocol);
        return 1;
    }

    return 0;
}

static void parse_tcp_packet(
    const struct pcap_pkthdr *packet_header,
    const u_char *packet_bytes,
    size_t network_offset,
    const struct ip *ip_header) 
{
    const struct tcphdr *tcp_header;
    const char *source_ip;
    const char *dest_ip;
    char source_ip_text[INET_ADDRSTRLEN];
    char dest_ip_text[INET_ADDRSTRLEN];
    uint16_t source_port;
    uint16_t dest_port;
    uint32_t payload_offset;
    uint32_t payload_length;

    tcp_header = (const struct tcphdr *)(packet_bytes + network_offset + (size_t)(ip_header->ip_hl * 4U));

    /* --- Reconstructed Missing Logic (Lines 79-99) --- */
    source_ip = inet_ntop(AF_INET, &(ip_header->ip_src), source_ip_text, INET_ADDRSTRLEN);
    dest_ip = inet_ntop(AF_INET, &(ip_header->ip_dst), dest_ip_text, INET_ADDRSTRLEN);

    source_port = ntohs(tcp_header->th_sport);
    dest_port = ntohs(tcp_header->th_dport);

    uint32_t ip_len = ntohs(ip_header->ip_len);
    uint32_t ip_header_size = ip_header->ip_hl * 4U;
    uint32_t tcp_header_size = tcp_header->th_off * 4U;

    payload_offset = network_offset + ip_header_size + tcp_header_size;

    if (ip_len >= ip_header_size + tcp_header_size) {
        payload_length = ip_len - (ip_header_size + tcp_header_size);
    /* --- End of Reconstructed Logic --- */
    } else {
        payload_length = 0;
    }

    printf(
        "tcp src=%s:%u dst=%s:%u seq=%u ack=%u payload=%u\n",
        source_ip,
        source_port,
        dest_ip,
        dest_port,
        ntohl(tcp_header->th_seq),
        ntohl(tcp_header->th_ack),
        payload_length);
}

static void handle_packet(
    u_char *user_data,
    const struct pcap_pkthdr *packet_header,
    const u_char *packet_bytes) 
{
    const struct ip *ip_header;
    uint16_t ether_type;
    size_t network_offset = 0;
    size_t ip_header_size;
    size_t tcp_offset;
    size_t tcp_header_size;

    (void)user_data;
    ++g_seen_packets;

    if (!get_network_offset_and_protocol(packet_header, packet_bytes, &network_offset, &ether_type)) {
        printf("packet %d unsupported_or_truncated_link_header\n", g_seen_packets);
        return;
    }

    if (ether_type != ETHERTYPE_IP) {
        printf("packet %d non-ip ether_type=0x%04x\n", g_seen_packets, ether_type);
        return;
    }

    if (packet_header->caplen < network_offset + sizeof(struct ip)) {
        printf("packet %d truncated before ip header\n", g_seen_packets);
        return;
    }

    ip_header = (const struct ip *)(packet_bytes + network_offset);
    ip_header_size = (size_t)(ip_header->ip_hl * 4U);
    if (ip_header_size < sizeof(struct ip)) {
        printf("packet %d invalid ip header length=%zu\n", g_seen_packets, ip_header_size);
        return;
    }

    if (packet_header->caplen < network_offset + ip_header_size) {
        printf("packet %d truncated inside ip header\n", g_seen_packets);
        return;
    }

    if (!is_tcp_packet(ip_header)) {
        printf("packet %d ip_non_tcp protocol=%u\n", g_seen_packets, (unsigned)ip_header->ip_p);
        return;
    }

    tcp_offset = network_offset + ip_header_size;
    if (packet_header->caplen < tcp_offset + sizeof(struct tcphdr)) {
        printf("packet %d truncated before tcp header\n", g_seen_packets);
        return;
    }

    tcp_header_size = (size_t)(((const struct tcphdr *)(packet_bytes + tcp_offset))->th_off * 4U);
    if (tcp_header_size < sizeof(struct tcphdr)) {
        printf("packet %d invalid tcp header length=%zu\n", g_seen_packets, tcp_header_size);
        return;
    }

    if (packet_header->caplen < tcp_offset + tcp_header_size) {
        printf("packet %d truncated inside tcp header\n", g_seen_packets);
        return;
    }

    ++g_tcp_packets;
    parse_tcp_packet(packet_header, packet_bytes, network_offset, ip_header);
}

int main(int argc, char **argv) {
    const char *interface_name = "lo";
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *handle;
    int datalink_type;
    int packet_limit = 10;

    if (argc >= 2) {
        interface_name = argv[1];
    }
    if (argc >= 3) {
        packet_limit = atoi(argv[2]);
        if (packet_limit <= 0) {
            packet_limit = 10;
        }
    }

    memset(errbuf, 0, sizeof(errbuf));
    g_datalink_type = 0;
    g_seen_packets = 0;
    g_tcp_packets = 0;

    handle = open_capture_handle(interface_name, errbuf);
    if (handle == NULL) {
        fprintf(stderr, "pcap_open_live failed: %s\n", errbuf);
        return 1;
    }

    datalink_type = pcap_datalink(handle);
    g_datalink_type = datalink_type;
    printf("interface=%s datalink=%s\n", interface_name, pcap_datalink_val_to_name(datalink_type));
    printf("libpcap=%s\n", pcap_lib_version());
    printf("capturing up to %d packets\n", packet_limit);

    if (datalink_type != DLT_EN10MB && datalink_type != DLT_LINUX_SLL) {
        fprintf(stderr, "This demo expects Ethernet or Linux cooked framing but saw %d\n", datalink_type);
        pcap_close(handle);
        return 1;
    }

    if (pcap_loop(handle, packet_limit, handle_packet, NULL) < 0) {
        fprintf(stderr, "pcap_loop failed: %s\n", pcap_geterr(handle));
        pcap_close(handle);
        return 1;
    }

    printf("summary seen=%d tcp=%d\n", g_seen_packets, g_tcp_packets);
    pcap_close(handle);
    return 0;
}