#include <stdio.h>
#include <stdlib.h>
int main(){
    int X = 1, x, n;
    scanf("%d %d", &x, &n);
    for (int i = 0; i < n; i++)
    {
        X *=  x;
    }

    printf("%d\n", X);
    return 0;
}
