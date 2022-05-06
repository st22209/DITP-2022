#include <stdio.h>

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%i", &num);

    for (int i = 1; i < num+1; i++)
    {
        printf("%i\n", i);
    }
    return 0;

}