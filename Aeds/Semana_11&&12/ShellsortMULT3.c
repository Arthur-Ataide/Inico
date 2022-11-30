#include "TadCartas.c"

/*
KE QE 8C JE 8E 1O 2O 8O 3O 6E 7O 1P 4C 10E
*/

int main(){
    Titem palavras[N], aux;
    int menor;
    
    inicia(palavras);

    int h = 6*3;
    int i, j, n;

    printf("\nSem mexer:\n");
    imprime(palavras);

    do {
       h = h/3;
       for(i = h; i < N; i++) {
        aux = palavras[i];
        j = i;
        
        while (palavras[j-h].num > palavras[j].num)
        {
            palavras[j] = palavras[j-h];
            j -= h;
            if (j<h) break;
        }
        palavras[j] = aux;

       }
    }
    while (h >= 1);

    printf("\nApenas o shell\n");

    imprime(palavras);

    insercao(palavras);

    printf("\nOrdenado com a insercao\n");

    imprime(palavras);
}
