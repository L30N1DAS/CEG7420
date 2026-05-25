#include "counter.h"
#include <stdio.h>

int shared_counter = 0; // global var
const int MAX_LIMIT = 32; // global var; const: value cannot be changed
static int file_private_total = 10; // static: limits visibility to only the code in this file

void increment_shared_counter(void) {
    shared_counter++;
    file_private_total += 5;
}

void print_private_total(void) {
    printf("file_private_total=%d\n", file_private_total);
}

void call_counter_demo(void) {
    static int counter_demo_calls = 0; // static: value persists across calls of the function
    counter_demo_calls++;
    printf("counter demo calls so far: %d\n", counter_demo_calls);
}
