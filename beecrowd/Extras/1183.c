#include <stdio.h>
#include <stdlib.h>

int main()
{
    double num = 0, soma = 0;
    char T;

    scanf("%c", &T);

    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            scanf("%lf", &num);
            if (j > i)
                soma += num;
        }
    }

    if(T == 'S')
        printf("%.1lf\n", soma);
    else
        printf("%.1lf\n", (soma/66));

    return 0;
}