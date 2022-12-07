#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 5

typedef struct {
    int num;
    char ind;
    char naipe;
} Titem;

void inicia(Titem *palavras);
void imprime(Titem *palavras);
void insercao(Titem *palavras);
void selecao(Titem *palavras);
void QuickSort(Titem *palavara, int tam);
void Ordena(int Esq, int Dir, Titem *palavras);
void Particao(int Esq, int Dir,int *i, int *j, Titem *palavras);
void HeapSort(Titem *palavras, int n);
void Constroi(Titem *palavras, int n);
void Refaz(int Esq, int Dir, Titem *palavras);
