#include <stdio.h>

int main() {
    for (int i = 18; i < 23; i++)
    {
        printf("%i\n", i);
    }

    printf("\n");

    for (int i = 0; i < 15; i = i + 2) 
    {
        printf("%i\n", i);
    }

    printf("\n");

    for (int i = 30; i != -15; i = i - 5)
    {
        printf("%i\n", i);
    }

    printf("\n");
    
    return 0;
}