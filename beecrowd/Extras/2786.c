#include <stdio.h>
#include <stdlib.h>

int main()
{
    int b, h, tipo1, tipo2;

    scanf("%d %d", &b, &h);

    tipo1 = (b * h) + ((b - 1) * (h - 1));
    tipo2 = 2 * (b - 1) + 2 * (h - 1);

    printf("%d\n%d\n", tipo1, tipo2);

    return 0;
}

