#include <stdio.h>
#include <stdlib.h>

int main()
{
    double num, soma = 0;
    int L;
    char T;

    scanf("%d %c", &L, &T);

    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            scanf("%lf", &num);
            if (i == L)
                soma += num;
        }
    }

    if(T == 'S')
        printf("%.1lf\n", soma);
    else
        printf("%.1lf\n", (soma/12));

    return 0;
}
