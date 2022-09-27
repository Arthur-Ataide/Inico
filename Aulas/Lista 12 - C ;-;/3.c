#include <stdio.h>
#include <stdlib.h>
int main(){
    int vetor[3];
    int x, a, b, c;
    scanf("%d", &x);
    a = x;
    c = x;
    b = x;
    vetor[0] = x;
    for (int i = 1; i < 3; i++)
    {
        scanf("%d", &x);
        vetor[i] = x;
        if(x>a) a = x;
        if(x < c) c = x;
    }
    for (int i = 1; i < 3; i++)
    {
        if (vetor[i] != a && vetor[i] != c) b = vetor[i];
    }
    printf("%d %d %d\n", a, b, c);
    return 0;
}
