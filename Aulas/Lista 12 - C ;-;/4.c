#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
    int x;
    scanf("%d", &x);
    if(x < 0) x = pow(x, 2);
    else x = sqrt(x);
    printf("%d\n", x);
    return 0;
}
