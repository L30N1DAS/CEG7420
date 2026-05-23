#include "config_reader.h"
#include <stdio.h>

int max = 10;

void print_config(const config_t *cfg) {
    printf("name=%s threshold=%d\n", cfg->name, cfg->threshold);
}

int threshold_is_high(const config_t *cfg) {
    return cfg->threshold >= max;
}