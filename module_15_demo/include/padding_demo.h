#ifndef PADDING_DEMO_H
#define PADDING_DEMO_H

typedef struct RecordEntry {
    char kind;
    int weight;
    short delta;
} RecordEntry;

typedef struct CompactRecord {
    int weight;         // 4 bytes
    short delta;        // 2 bytes
    char kind;          // 1 byte
    char code;          // 1 byte
} CompactRecord;

typedef struct WideHeader {
    char flag;          // 1 byte
    double value;       // 8 bytes
    short code;         // 2 bytes
} WideHeader;

#endif