#include "TadCartas.c"

/*
KE QE 8C JE 8E 1O 2O 8O 3O 6E 7O 1P 4C 10E
4K 1E 5U 2O 3E
*/

int main(){

    Titem palavras[N];
    int tam = N;

    inicia(palavras);

    HeapSort(palavras, tam);

    printf("\nOrdenando: \n");

    imprime(palavras);

    return 0;

}