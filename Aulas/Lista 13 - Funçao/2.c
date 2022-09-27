#include <stdio.h>
#include <stdlib.h>

int par_imp(int);

int main()
{
    int x;
    scanf("%d", &x);
    if (par_imp(x) == 0)
        printf("O numero e par");
    else
        printf("O numero e impar");
    return 0;
}

int par_imp(int x)
{   if (x % 2 == 0)
        return 0;
    else
        return 1;
}
