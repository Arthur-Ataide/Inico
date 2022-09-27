#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int tri(int, int, int);

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    tri(a, b, c);
    return 0;
}

int tri(int a, int b, int c)
{   
    if (a == b && a == c)
        {
        printf("equilatero");
        return 0;
        }
    if (a == b || a == c || c ==b)
        {
        printf("isosceles");
        return 0;
        }
    else
        {
            printf("escaleno");
            return 0;
        }
}
