#include <stdio.h>
#include <stdlib.h>

impar(int, int);

int main()
{
    impar(0, 100);
    return 0;
}

impar(int zero, int cem)
{   
    if (zero % 2 == 0)
    {
        zero++;
        printf("%d\n", zero);
    }
    zero += 2;

    if (zero < cem)
    {
        printf("%d\n", zero);
        impar(zero, cem);
    }
}
