#include <stdio.h>
#include <stdlib.h>

// 4 5 1 3 7 3 8 3 6 0

int main(){
    int vetor[10];
    int h = 1;
    int aux, i, j, n;
    n = 10;
    
    for (int c = 0; c < 10; c++){
        scanf("%d", &vetor[c]);
    }

    for (int c = 0; c < 10; c++){
        printf("%d ", vetor[c]);
    }
    printf("\n");
    
    
    do h = h * 3 + 1; 
    while (h<n);

    do {
       h = h/3;
       for(i = h; i < n; i++) {
        aux = vetor[i];
        j = i;
        
        while (vetor[j-h] > vetor[j])
        {
            vetor[j] = vetor[j-h];
            j -= h;
            if (j<h) break;
        }
        vetor[j] = aux;

       }
    }
    while (h >= 1);

    printf("%d\n", h);

    for (int c = 0; c < 10; c++){
        printf("%d ", vetor[c]);
        }

    printf("\n");
}
