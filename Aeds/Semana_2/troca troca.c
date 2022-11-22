#include <stdio.h>

void troca_troca(int*, int*, int*);

int main(){
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);

    troca_troca(&a, &b, &c);

    printf("%d %d %d", a, b, c);
    
}

void troca_troca(int* a, int* b ,int* c){
    int aux;

    aux = *a;
    *a = *c;
    *c = *b;
    *b = aux;
}

