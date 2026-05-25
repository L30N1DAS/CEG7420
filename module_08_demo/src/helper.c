#include "counter.h"
#include "helper.h"
#include <stdio.h>

void helper_report(void) {
    shared_counter += 1;
    increment_shared_counter();
    printf("helper_report: shared_counter=%d, MAX_LIMIT=%d\n",
           shared_counter,
           MAX_LIMIT);

    /* This would fail to compile because MAX_LIMIT is const. */
    /* MAX_LIMIT = 99; */
}
