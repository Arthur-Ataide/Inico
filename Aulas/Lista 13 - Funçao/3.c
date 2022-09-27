#include <stdio.h>
#include <stdlib.h>

int primo(int);

int main()
{
    int x;
    scanf("%d", &x);
    if (primo(x) == 0)
        printf("O numero e primo");
    else
        printf("O numero nao e primo");
    return 0;
}

int primo(int x)
{   
    int cont = 0;
    for (int i = 1; i < x; i++)
    {
        if (x % i == 0)
        {
            cont++;
        }
    }
    if (cont == 1)
        return 0;
    else
        return 1;
}
