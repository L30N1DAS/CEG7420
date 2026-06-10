typedef int bpf_int32;
typedef u_int bpf_u_int32;

typedef struct timeval {
    long tv_sec;
    long tv_usec;
} timeval;

struct pcap_pkthdr {
    struct timeval ts;      /* time stamp */
    bpf_u_int32 caplen;     /* length of portion present */
    bpf_u_int32 len;        /* length this packet (off wire) */
};