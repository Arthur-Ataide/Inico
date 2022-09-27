#include <stdio.h>
#include <stdlib.h>

int asterisco(int, int);

int main()
{
    int x;

    scanf("%d", &x);
    asterisco(x, x);

    return 0;
}

int asterisco(int x, int n)
{
    for (int i = 0; i < x; i++)
    {
        printf("*");
    }

    printf("\n");
    n--;

    if (n == 0)
        return 0;

    else
        return asterisco(x, n);
}
