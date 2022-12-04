#include "TadCartas.c"

/*
KE QE 8C JE 8E 1O 2O 8O 3O 6E 7O 1P 4C 10E
4K 1E 3U 2O
*/

int main(){

    Titem palavras[N];
    int tam;

    inicia(palavras);

    QuickSort(palavras, N);

    printf("\nOrdenando: \n");

    imprime(palavras);

    return 0;

}