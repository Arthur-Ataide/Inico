#include <stdio.h>
#include <math.h>

int main()
{

    int n, num;

    scanf("%d", &n);
    if (n % 2 != 0)
        n --;

    for (int i = 2; i < n+1; i+=2)
    {   
        num = pow(i,2);
        printf("%d^2 = %d\n", i, num);
    }
    
    return 0;

}