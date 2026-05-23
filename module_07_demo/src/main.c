#include "config_reader.h"
#include <stdio.h>

int main(void) {
    config_t demo = {"demo-mode", max + 2};
    print_config(&demo);
    printf("max=%d high=%s\n",
           max,
           threshold_is_high(&demo) ? "yes" : "no");
    return 0;
}