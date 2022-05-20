#include <stdio.h>

int main()
{  
    int total = 0;

    for (int i = 0; i < 101; i++)
    {
        total = total + i;
    }
    float average = (float)total / 100;
    printf("Total %i\nAverage: %.2f\n", total, average);
    
    return 0;
}