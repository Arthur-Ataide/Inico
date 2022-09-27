#include <stdio.h>
#include <stdlib.h>
int main(){
    int vetor[13];
    int cont = 1;
    int pro = 4;
    
    for (int i = 0; i < 13; i++)
    {
        if(i % 3 == 0){
        vetor[i] = cont;
        cont ++;
            if (i != 0) pro ++;
        }
        else {vetor[i] = pro;
         vetor[i+1] = pro;
        }
    }
    printf("%d\n", vetor[12]);
    return 0;
}
