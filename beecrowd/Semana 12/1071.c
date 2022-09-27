#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x, y, maior, menor, soma;
    soma = 0;

    scanf("%d %d", &x, &y);
    maior = x;
    menor = y;

    if (maior < y)
        {
        maior = y;
        menor = x;
        }

    for (int i = menor+1; i < maior; i++)
    {   
        if (i % 2 != 0)
            soma += i;
    }

    printf("%d\n", soma);

    return 0;
}