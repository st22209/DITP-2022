#include <stdio.h>

int max(int a, int b, int c);

int main()
{
    int answer = max(214, 523, 123);
    printf("The max value is: %i\n", answer);
    
    return 0;
}

int max(int a, int b, int c)
{
    if (a > b && a > c)
    {
        return a;
    } else if (b > a && b > c)
    {
        return b;
    } else if (c > a && c > b)
    {
        return c;
    }
    
}