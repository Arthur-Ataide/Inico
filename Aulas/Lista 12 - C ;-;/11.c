#include <stdio.h>
#include <stdlib.h>
int main(){
    int vetor[10], vetor2[10];

    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &vetor[i]);
    }

    for (int i = 0; i < 10; i++)
    {
        if (i == 9) printf("%d\n", vetor[i]);
        else printf("%d ", vetor[i]);
    }
    for (int i = 0; i < 10; i++)
    {
        if (vetor[i] < 10) vetor2[i] = 1;
        else vetor2[i] = vetor[i];
        if (i == 9) printf("%d\n", vetor2[i]);
        else printf("%d ", vetor2[i]);
    }
    return 0;
}
