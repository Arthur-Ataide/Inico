#include <stdio.h>
#include <stdlib.h>

int MDC(int, int);

int main()
{
    int x, y;

    scanf("%d %d", &x, &y);
    printf("%d",MDC(x, y));

    return 0;
}

int MDC(int x, int y)
{   
    if (x == y)
        return x;
    if (x > y)
        MDC(x - y, y);
    else
        MDC(y - x, x);

}
