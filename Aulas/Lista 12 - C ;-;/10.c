#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, soma = 0;
    scanf("%d", &n);
    int vetor[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &vetor[i]);
        if (vetor[i]%2==0) soma+=vetor[i];
    }
    printf("%d", soma);
    return 0;
}
