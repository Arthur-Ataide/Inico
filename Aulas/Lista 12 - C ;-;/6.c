#include <stdio.h>
#include <stdlib.h>
int main(){
    double soma;
    int cont = 1;
    for (int i = 37; i > 0; i--)
    {
        soma = (i * (i+1))/cont;
        cont++;
    }
    printf("%.2lf", soma);
    return 0;
}
