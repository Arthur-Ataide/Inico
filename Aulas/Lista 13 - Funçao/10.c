#include <stdio.h>
#include <stdlib.h>

int menor(int, int, int);

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d", menor(a, b, c));
    return 0;
}

int media(int a, int b, int c)
{   
    int menor = a;
    if (menor > b)
        menor = b;
    if (menor > c)
        menor = c;

    return menor;
}
