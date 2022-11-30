#include "TadCartas.h"

// 1P 5C 3O 1C 1E 1O 2O KO 3O
// KE QE 8C JE 8E 1O 2O 8O 3O

void inicia(Titem *palavras){
    
    char carta[4];

    for(int i = 0; i < N; i++){

        printf("Digite a carta %d\n", i+1);
        scanf("%s", carta);        
        
        if (strlen(carta) == 3){
            palavras[i].num = 10;
            palavras[i].naipe = carta[2];
        }

        else{
            switch (carta[0]){
            case 'Q':
                palavras[i].num = 11;
                break;

            case 'J':
                palavras[i].num = 12;
                break;

            case 'K':
                palavras[i].num = 13;
                break;
            
            default:
                palavras[i].num = carta[0] - '0';
                break;
            }
            palavras[i].naipe = carta[1];
            palavras[i].ind = carta[0];
        }
    }   
}

void imprime(Titem *palavras){
    
    for(int i = 0; i < N; i++){
        if (palavras[i].num <= 10){
            printf("%d%c ", palavras[i].num, palavras[i].naipe);
        }
        else{
            printf("%c%c ", palavras[i].ind, palavras[i].naipe);
        }
        
    }
    printf("\n");
}

void insercao(Titem *palavras){
    Titem aux;
    int i,j;
    
    for (i = 1; i < N; i++){
            aux = palavras[i];
            j = i - 1;
        while ( ( j >= 0 ) && ( aux.num < palavras[j].num ) ){
            palavras[j + 1] = palavras[j];
            j--;
        }
        palavras[j + 1] = aux;
    }
}

void selecao(Titem * palavras){
    Titem aux;
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
}
