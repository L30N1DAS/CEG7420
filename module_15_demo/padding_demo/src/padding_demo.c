#include "padding_demo.h"

#include <stddef.h>
#include <stdio.h>

static void show_record_entry_layout(const RecordEntry *record)
{
    printf("RecordEntry\n");
    printf("sizeof(RecordEntry)=%zu\n", sizeof(RecordEntry));
    printf("sizeof(kind)=%zu\n", sizeof(record->kind));
    printf("sizeof(weight)=%zu\n", sizeof(record->weight));
    printf("sizeof(delta)=%zu\n", sizeof(record->delta));
    printf("record=%p\n", (void *)record);
    printf("&record->kind=%p\n", (void *)&record->kind);
    printf("&record->weight=%p\n", (void *)&record->weight);
    printf("&record->delta=%p\n", (void *)&record->delta);
    printf("offset(kind)=%zu\n", offsetof(RecordEntry, kind));
    printf("offset(weight)=%zu\n", offsetof(RecordEntry, weight));
    printf("offset(delta)=%zu\n", offsetof(RecordEntry, delta));
    printf("\n");
}

static void show_compact_record_layout(const CompactRecord *record)
{
    printf("CompactRecord\n");
    printf("sizeof(CompactRecord)=%zu\n", sizeof(CompactRecord));
    printf("sizeof(weight)=%zu\n", sizeof(record->weight));
    printf("sizeof(delta)=%zu\n", sizeof(record->delta));
    printf("sizeof(kind)=%zu\n", sizeof(record->kind));
    printf("sizeof(code)=%zu\n", sizeof(record->code));
    printf("record=%p\n", (void *)record);
    printf("&record->weight=%p\n", (void *)&record->weight);
    printf("&record->delta=%p\n", (void *)&record->delta);
    printf("&record->kind=%p\n", (void *)&record->kind);
    printf("&record->code=%p\n", (void *)&record->code);
    printf("offset(weight)=%zu\n", offsetof(CompactRecord, weight));
    printf("offset(delta)=%zu\n", offsetof(CompactRecord, delta));
    printf("offset(kind)=%zu\n", offsetof(CompactRecord, kind));
    printf("offset(code)=%zu\n", offsetof(CompactRecord, code));
    printf("\n");
}

static void show_wide_header_layout(const WideHeader *record)
{
    printf("WideHeader\n");
    printf("sizeof(WideHeader)=%zu\n", sizeof(WideHeader));
    printf("sizeof(flag)=%zu\n", sizeof(record->flag));
    printf("sizeof(value)=%zu\n", sizeof(record->value));
    printf("sizeof(code)=%zu\n", sizeof(record->code));
    printf("record=%p\n", (void *)record);
    printf("&record->flag=%p\n", (void *)&record->flag);
    printf("&record->value=%p\n", (void *)&record->value);
    printf("&record->code=%p\n", (void *)&record->code);
    printf("offset(flag)=%zu\n", offsetof(WideHeader, flag));
    printf("offset(value)=%zu\n", offsetof(WideHeader, value));
    printf("offset(code)=%zu\n", offsetof(WideHeader, code));
    printf("\n");
}

int main(void)
{
    RecordEntry record_entry = {
        .kind = 'R',
        .weight = 100,
        .delta = 3,
    };

    CompactRecord compact_record = {
        .weight = 200,
        .delta = 4,
        .kind = 'C',
        .code = 'Z',
    };

    WideHeader wide_header = {
        .flag = 'W',
        .value = 3.14159,
        .code = 9,
    };

    show_record_entry_layout(&record_entry);
    show_compact_record_layout(&compact_record);
    show_wide_header_layout(&wide_header);

    record_entry.kind = 'A';
    record_entry.weight = 300;
    record_entry.delta = 0;

    return 0;
}