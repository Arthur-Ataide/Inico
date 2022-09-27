#include <stdio.h>
#include <stdlib.h>

int MOD(int, int);

int main()
{
    int x, y;

    scanf("%d %d", &x, &y);
    printf("%d",MOD(x, y));

    return 0;
}

int MOD(int x, int y)
{   
    if (x < y)
        return x;
    
    if (x == y)
        return 0;

    return (MOD(x - y, y));

}
