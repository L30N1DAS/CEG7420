#include "struct_demo.h"

#include <stdio.h>
#include <stdlib.h>

//one/single record as global. .data section
static RecordEntry global_record = {
    .kind = 'G',
    .weight = 10,
    .delta = 3,
};

//one array of records (3 records) as global. .data section
static RecordEntry global_records[] = {
    {'A', 10, 1},
    {'B', 20, 2},
    {'C', 30, 3},
};

static int score_single_record(const RecordEntry *record)
{
    return (int)record->kind + record->weight - record->delta;
}

static int score_record_array(const RecordEntry *records, size_t count)
{
    int total = 0;
    size_t i;

    for (i = 0; i < count; ++i) {
        total += records[i].weight + records[i].delta;
    }

    return total;
}

int score_global_single_record(void)
{
    return score_single_record(&global_record);
}

int score_global_record_array(void)
{
    return score_record_array(
        global_records, sizeof(global_records) / sizeof(global_records[0]));
}

int score_stack_single_record(int seed)
{
    RecordEntry local_record = {
        .kind = 'S',
        .weight = seed + 7,
        .delta = (short)(seed & 3),
    };

    return score_single_record(&local_record);
}

int score_stack_record_array(int seed)
{
    RecordEntry local_records[3] = {
        {'L', seed + 1, 1},
        {'M', seed + 2, 2},
        {'N', seed + 3, 3},
    };

    return score_record_array(local_records, 3);
}

int score_heap_single_record(int seed)
{
    RecordEntry *heap_record;
    int result;

    heap_record = (RecordEntry *)malloc(sizeof(RecordEntry));
    if (heap_record == NULL) {
        return -1;
    }

    heap_record->kind = 'H';
    heap_record->weight = seed + 11;
    heap_record->delta = (short)(seed % 5);

    result = score_single_record(heap_record);
    free(heap_record);
    return result;
}

int score_heap_record_array(int seed)
{
    RecordEntry *heap_records;
    int result;
    size_t i;
    size_t count = 3;

    heap_records = (RecordEntry *)malloc(count * sizeof(RecordEntry));
    if (heap_records == NULL) {
        return -1;
    }

    for (i = 0; i < count; ++i) {
        heap_records[i].kind = (char)('a' + (int)i);
        heap_records[i].weight = seed + (int)i + 1;
        heap_records[i].delta = (short)(i + 1);
    }

    result = score_record_array(heap_records, count);
    free(heap_records);
    return result;
}

int main(void)
{
    printf("global_single=%d\n", score_global_single_record());
    printf("global_array=%d\n", score_global_record_array());
    printf("stack_single=%d\n", score_stack_single_record(7));
    printf("stack_array=%d\n", score_stack_record_array(7));
    printf("heap_single=%d\n", score_heap_single_record(9));
    printf("heap_array=%d\n", score_heap_record_array(9));
    return 0;
}