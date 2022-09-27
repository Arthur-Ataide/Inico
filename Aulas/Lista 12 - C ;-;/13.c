#include <stdio.h>
#include <stdlib.h>
int main(){
    int matrix[10][10];

    for (int i = 0; i < 10; i++)
    {
        for(int j =0; j < 10; j++)
        {
            scanf("%d", &matrix[i][j]);
            if (i == j) printf("%d ", matrix[i][j]);
        }
    }
    return 0;
}
