#include <stdio.h>

int c;

int main() {
    int n, i, c = 0;

    for (n = 25; n <= 50; n++){
        for (i = 1; i <= n; i++) {
            if (n % i == 0) {
                c++;
            }
        }
        if (c == 2) {
            printf("%i is a Prime number\n", n);
        }
        else {
            printf("%i is not a Prime number\n", n);
        }
        c = 0;
    }

    return 0;
}