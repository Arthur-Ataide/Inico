#include <stdio.h>
#include <stdlib.h>

float media(int, int, int);

int main()
{
    int a, b, c;
    float nota;
    scanf("%d %d %d", &a, &b, &c);
    nota = media(a, b, c);
    printf("%f", nota);
    return 0;
}

float media(int a, int b, int c)
{   
    float nota;
    nota = (a + b + c)/3;
    return nota;
}
