#include <stdio.h>
#include <stdlib.h>
int main(){
    int a, b, x;
    while (a != -1 && b != -1)
    {
        scanf("%d %d", &a, &b);
        x = a + b;
        printf("X = %d\n", x);
    }
    return 0;
}
