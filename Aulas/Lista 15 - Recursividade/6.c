#include <stdio.h>
#include <stdlib.h>

int fatorial(int);

int main()
{
    int x;

    scanf("%d", &x);
    printf("%d",fatorial(x));

    return 0;
}

int fatorial(int x)
{   
    int fat;

    if (x == 1)
        return 1;

    fat = x * fatorial(x-1);
    return fat;
}
