#include <stdio.h>

int main() 
{
    int number;

    printf("Enter the width: ");
    scanf("%i", &number);

    for (int i = 0; i < number; i++)
    {
        for (int x = 0; x < (i+1); x++)
        {
            printf("%i", (x+1));
        }
        printf("\n");
    }
    
    return 0;
}