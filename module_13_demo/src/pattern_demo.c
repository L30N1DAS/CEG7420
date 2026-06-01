#include <stdio.h>

int sum_and_check(int a, int b) {
    int x = a + b;
    if (x == 10) {
        return 1;
    }
    return 0;
}

int loop_accumulate(void) {
    int total = 0;
    for (int i = 0; i < 4; i++) {
        total += i;
    }
    return total;
}

int read_array_value(const int *array, int index) {
    return array[index];
}

int classify_char(const char *s) {
    unsigned char c = (unsigned char)s[0];

    if (c == 0) {
        return 0;
    }
    if (c & 1) {
        return 1;
    }
    if (c == 'A') {
        return 2;
    }
    return 3;
}

int main(void) {
    int values[4] = {3, 5, 7, 9};
    int result = sum_and_check(4, 6);
    int total = loop_accumulate();
    int picked = read_array_value(values, 2);
    int kind = classify_char("A");

    if (result && total == 6 && picked == 7 && kind == 1) {
        puts("branch hit");
    }

    return 0;
}