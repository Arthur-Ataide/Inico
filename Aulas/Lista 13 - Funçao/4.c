#include <stdio.h>
#include <stdlib.h>

int invert(int);

int main()
{
    int num;
    scanf("%d", num);
    printf("%d", num%10);
    return 0;
}

int invert(int num)
{
    int x, aux1, aux2;
    aux1 = num % 10;
    x = aux1 * 100;
    aux2 = (num % 100);
    x += aux2 - aux1;
    x += (num - aux2) / 10;
    
    return x;
}
