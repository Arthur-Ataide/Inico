#include <stdio.h>

int main()
{   
    int dinheiros[7], n, cont = 0;

    int vetor[7] = {100, 50, 20, 10, 5, 2, 1};

    scanf("%d", &n);
    printf("%d\n", n);
    for (int i = 0; i < 7; i++)
    {   
        dinheiros[i] = n / vetor[i];
        n = n % vetor[i];
    }
    
    for (int i = 0; i < 7; i++)
    {
        printf("%d nota(s) de R$ ", dinheiros[i]);
        if (cont == 0)
            printf("100,00\n");  
        if (cont == 1)
            printf("50,00\n");
        if (cont == 2)
            printf("20,00\n");
        if (cont == 3)
            printf("10,00\n");
        if (cont == 4)
            printf("5,00\n");
        if (cont == 5)
            printf("2,00\n");
        if (cont == 6)
            printf("1,00\n");
        cont++;

    }
    return 0;

}