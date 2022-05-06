#include <stdio.h>

int main() {
    int start, stop, increment;

    printf("Enter the start number: ");
    scanf("%i", &start);

    printf("Enter the stop number: ");
    scanf("%i", &stop);

    printf("Enter the increment amount: ");
    scanf("%i", &increment);

    for (int i = start; i < stop+1; i = i + increment)
    {
        printf("%i\n", i);
    }
}