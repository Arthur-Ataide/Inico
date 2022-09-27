#include <stdio.h>
#include <stdlib.h>

int DIV(int, int);

int main()
{
    int x, y;

    scanf("%d %d", &x, &y);
    printf("%d",DIV(x, y));

    return 0;
}

int DIV(int x, int y)
{   
    if (x < y)
        return 0;
    
    if (x == y)
        return 1;

    return (1 + DIV(x - y, y));

}
