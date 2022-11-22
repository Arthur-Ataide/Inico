#include "TadCartas.h"

int main(){
    Titem palavras[9];
    char carta[2];

    for(int i = 0; i < 9; i++){
        printf("Digite a carta %d\n", i+1);
        scanf("%s", carta);
        
        switch (carta[0])
        {
        case 'K':
            
            break;
        
        default:
            break;
        }
        palavras[i].num = carta[0];
        palavras[i].naipe = carta[1];
    }    
    return 0;
}