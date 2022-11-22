#include <stdio.h>

void zerar(int*, int*);

int main(){
    int x, y;

    scanf("%d %d", &x, &y);
    zerar(&x, &y);

    printf("%d %d", x, y);
    return 0;

}

void zerar(int* x, int* y){
    (*x) = 0;
    (*y) = 0;
}