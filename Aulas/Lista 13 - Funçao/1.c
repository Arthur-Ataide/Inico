#include <stdio.h>
#include <stdlib.h>

int delta(int, int, int);
int raiz_mais(int, int, int);
int raiz_menos(int, int, int);

int main()
{
    int a, b, c, D;
    scanf("%d %d %d", &a, &b, &c);
    D = delta(a, b, c);
    printf("Delta = %d\n", D);
    if (D >= 0)
    {
        printf("X1 = %d\n", raiz_mais(a, b, D));
        printf("X2 = %d\n", raiz_menos(a, b, D));
    }
    else
        printf("Nao existe raiz");
        
    return 0;
}

int delta(int a, int b, int c)
{   int valor = b*b - (4 * a * c);
    return valor;
}

int raiz_mais(int a, int b, int D)
{
    return (-b + D)/2*a; 
}

int raiz_menos(int a, int b, int D)
{
    return (-b - D)/2*a; 
}
