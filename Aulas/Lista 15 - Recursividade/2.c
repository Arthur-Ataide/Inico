#include <stdio.h>
#include <stdlib.h>

multiplos(int, int);

int main()
{
    int x, y;

    scanf("%d %d", &x, &y);
    multiplos(x, y);

    return 0;
}

multiplos(int x, int y)
{   
    if (x % 5 != 0)
    {  
        x += 5 - (x % 5);
        if (x < y)
        {
            printf("%d\n", x);
        }
    }

    if (x + 5 < y)
    {   
        x += 5;
        printf("%d\n", x);
        multiplos(x, y);
    }

}
