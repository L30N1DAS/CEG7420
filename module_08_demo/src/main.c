#include "counter.h"
#include "helper.h"
#include <stdio.h>

int main(void) {
    printf("MAX_LIMIT=%d\n", MAX_LIMIT);

    increment_shared_counter();
    printf("shared_counter=%d\n", shared_counter);

    helper_report();
    helper_report();

    call_counter_demo();
    call_counter_demo();

    print_private_total();

    return 0;
}
