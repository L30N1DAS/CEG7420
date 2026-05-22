#include <stdio.h>
#include <string.h>

static const char *secret = "open-sesame";
static const char *log_path = "/tmp/re_demo.log";

static void log_attempt(const char *user_input, int ok) {
    FILE *fp = fopen(log_path, "a");
    if (fp != NULL) {
        fprintf(fp, "input=%s result=%d\n", user_input, ok);
        fclose(fp);
    }
}

int check_access(const char *user_input) {
    return strcmp(user_input, secret) == 0;
}

int main(int argc, char **argv) {
    puts("Reverse engineering demo");

    if (argc < 2) {
        puts("usage: ./intro_analysis_demo <key>");
        return 1;
    }

    int ok = check_access(argv[1]);
    log_attempt(argv[1], ok);

    if (ok) {
        printf("Access granted for %s\n", argv[1]);
        return 0;
    }

    puts("Access denied");
    return 2;
}