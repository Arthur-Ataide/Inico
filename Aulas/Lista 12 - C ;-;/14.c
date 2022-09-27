#include <stdio.h>
#include <stdlib.h>
int main(){
    int matrix[3][5], vetor[3];
    vetor[0] = 0;
    vetor[1] = 0;
    vetor[2] = 0;

    for (int i = 0; i < 3; i++)
    {
        for(int j =0; j < 5; j++)
        {
            scanf("%d", &matrix[i][j]);
            vetor[i]+= matrix[i][j];
        }
        printf("%d ",vetor[i]);
    }
    return 0;
}
