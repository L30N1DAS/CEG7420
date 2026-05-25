#ifndef COUNTER_H
#define COUNTER_H

// extern: distinguishes a declaration from a definition
extern int shared_counter;
extern const int MAX_LIMIT;

// extern is optional for functions since the function body suffices to differentiate a declaration from a definition
extern void increment_shared_counter(void);
extern void print_private_total(void);
extern void call_counter_demo(void);

#endif
