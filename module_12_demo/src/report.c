#include <report.h>
#include <stdio.h>

int initialized_count = 7;
int pending_count;
const char banner[] = "ELF demo";
static const char status_text[] = "ready";

static int next_count(void) {
    return pending_count + 1;
}

void show_report(void) {
    pending_count = next_count();
    printf("%s %s init=%d pending=%d\n",
           banner, status_text, initialized_count, pending_count);
}