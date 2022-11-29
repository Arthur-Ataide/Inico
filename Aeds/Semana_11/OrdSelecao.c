#include "TadCartas.c"


// 1P 5C 3O 1C 1E 1O 2O KO 3O
int main(){
    
    Titem palavras[N], aux;
    int menor;
    
    inicia(palavras);

    for (int i = 0; i < N-1; i++){
        menor = i;
        for(int j = i+1; j < N; j++)
            if (palavras[menor].num > palavras[j].num)
                menor = j;
        aux = palavras[menor];
        palavras[menor] = palavras[i];
        palavras[i] = aux;
    }

    for(int i = 0; i < N; i++){
        printf("%c%c ", palavras[i].ind, palavras[i].naipe);
    }
    printf("\n");

    return 0;
}