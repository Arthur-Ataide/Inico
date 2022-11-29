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
            palavras[i].naipe = carta[3];
            break;
        }

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
