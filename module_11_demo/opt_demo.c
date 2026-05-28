#include <stdio.h>

/*
 * Optimization levels demo:
 * -O0 : no optimization, preserves all structures.
 * -O1 : basic optimization.
 * -Og : optimize for debugging experience.
 * -O2 : further reshapes the loop in compute_sum().
 * -O3 : may apply more aggressive loop and inlining decisions than -O2.
 * -Os : optimizes for size, often keeping many of the simplifications from -O2.
 * -Oz : optimizes even more aggressively for size when supported by the toolchain.
 *
 * These are observed behaviors for this compiler/toolchain, not language
 * guarantees for every compiler in every configuration.
 */

static int multiply_by_two(int x) {
    return x * 2;
}

/*
 * This function is never called.
 * Observed here:
 * -O0: the function symbol appears in the binary.
 * -Og: usually still keeps some debug-friendly structure, but may remove it.
 * -O1/-O2/-O3: the compiler removes it entirely.
 * -Os/-Oz: usually removes it entirely as well.
 */
static int unused_function(void) {
    return 99;
}

int compute_sum(int limit) {
    int sum = 0;
    int impossible = limit - limit;

    for (int i = 0; i < limit; i++) {
        sum += multiply_by_two(i);
    }

    /*
     * This block is logically dead because impossible is always 0.
     * Observed here:
     * -O0: GCC keeps the compare and branch in the emitted code.
     * -Og: may still simplify this, depending on the compiler's debug-oriented choices.
     * -O1/-O2/-O3: GCC folds impossible to 0 and removes this block.
     * -Os/-Oz: usually removes this block too.
     */
    if (impossible != 0) {
        printf("dead block: %d\n", impossible);
        sum += 1000;
    }

    return sum;
}

int main(void) {
    /*
     * Observed here:
     * -O0: multiply_by_two() remains a separate local function symbol.
     * -Og: may or may not inline, depending on debug-oriented heuristics.
     * -O1/-O2/-O3: GCC inlines multiply_by_two() in this example.
     * -Os/-Oz: may inline it if that still helps code size or overall simplification.
     *
     * In general:
     * - lower levels preserve source structure better
     * - higher levels reshape code more aggressively
     * - size-oriented levels still remove dead code aggressively
     */
    int value = multiply_by_two(5);
    int sum = compute_sum(5);

    printf("value=%d\n", value);
    printf("sum=%d\n", sum);

    return 0;
}