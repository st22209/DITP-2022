#include <stdio.h>

int main() 
{
    int width;

    printf("Enter the width: ");
    scanf("%i", &width);

    for (int i = width-1; i != -1; i--)
    {
        for (int x = i+1; x != 0; x--) 
        {
            printf("%i ", x);
        }
        printf("\n");
    }
    return 0;
}
//  for i in (0..(width+1)).rev() {
//         for x in (1..(i+1)).rev() {
//             print!("{}", x)
//         }
//         println!();
//     }