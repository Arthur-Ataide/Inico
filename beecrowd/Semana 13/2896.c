#include <stdio.h>
 


int main() {
    int t, n, k, garrafa;

    scanf("%d", &t);

    for (int i = 0; i < t; i++)
    {
        scanf("%d", &n);
        scanf("%d", &k);

        garrafa = (n / k) + (n % k);
        printf("%d\n", garrafa);

    }
 
    return 0;
}