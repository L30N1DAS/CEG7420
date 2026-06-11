#ifndef STRUCT_DEMO_H
#define STRUCT_DEMO_H

typedef struct RecordEntry {
    char kind;          // 1 byte + 3 bytes padding
    int weight;         // 4 bytes
    short delta;        // 2 bytes + 2 bytes padding
} RecordEntry;

int score_global_single_record(void);
int score_global_record_array(void);

int score_stack_single_record(int seed);
int score_stack_record_array(int seed);

int score_heap_single_record(int seed);
int score_heap_record_array(int seed);

#endif