#include <stdio.h>
#include <stdlib.h>

int main(){
    double x, A, n;
    n = 3.14159;
    scanf("%lf", &x);
    A = x * x * n;
    printf("A=%.4lf\n", A);
    return 0;
}
