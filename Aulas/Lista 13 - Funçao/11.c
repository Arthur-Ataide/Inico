#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int area(int, int, int);

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d", area(a, b, c));
    return 0;
}

int media(int a, int b, int c)
{   
    int p;
    p = (a + b+ c)/2;
    return sqrt(p*(p-a)*(p-b)*(p-c));
}
