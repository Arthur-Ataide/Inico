#include <stdio.h>
#include <stdlib.h>

int main() {
    int num, matrix[3][3];

    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++){
            scanf("%d", &num);
            matrix[i][j] = num;
        }


    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            printf("%d ", matrix[i][j]);

    return 0;
}
