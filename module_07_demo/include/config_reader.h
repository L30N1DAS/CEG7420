#ifndef CONFIG_READER_H
#define CONFIG_READER_H

typedef struct {
    const char *name;
    int threshold;
} config_t;

extern int max;

void print_config(const config_t *cfg);
int threshold_is_high(const config_t *cfg);

#endif