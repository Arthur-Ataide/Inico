#include "TadCartas.c"
/*
KE QE 8C JE 8E 1O 2O 8O 3O
KE QE 8C JE 8E 1O 2O 8O 3O 6E 7O 1P 4C 10E
*/

int main(){
    
    Titem palavras[N], aux;
    int i,j;

    inicia(palavras);
    

    
    for (i = 1; i < N; i++){
            aux = palavras[i];
            j = i - 1;
        while ( ( j >= 0 ) && ( aux.num < palavras[j].num ) ){
            palavras[j + 1] = palavras[j];
            j--;
        }
        palavras[j + 1] = aux;
    }

    imprime(palavras);

    return 0;
}