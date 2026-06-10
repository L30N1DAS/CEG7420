#ifndef PADDING_DEMO_H
#define PADDING_DEMO_H

typedef struct RecordEntry {
    char kind;
    int weight;
    short delta;
} RecordEntry;

typedef struct CompactRecord {
    int weight;
    short delta;
    char kind;
    char code;
} CompactRecord;

typedef struct WideHeader {
    char flag;
    double value;
    short code;
} WideHeader;

#endif