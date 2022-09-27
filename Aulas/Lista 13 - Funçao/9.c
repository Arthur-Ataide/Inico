#include <stdio.h>
#include <stdlib.h>

int sinal(int);

int main()
{
    int x;
    scanf("%d", &x);
    if (sinal(x) == 0)
        printf("Positivo");
    else
        printf("Negativo");
    return 0;
}

int sinal(int x)
{   if (x >= 0)
        return 0;
    else
        return 1;
}
