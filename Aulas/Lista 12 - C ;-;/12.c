#include <stdio.h>
#include <stdlib.h>
int main(){
    int vetor1[10], vetor2[10], cont;
    cont = 9;
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &vetor1[i]);
        vetor2[cont] = vetor1[i];
        cont--;
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", vetor2[i]);
    }

    return 0;
}
