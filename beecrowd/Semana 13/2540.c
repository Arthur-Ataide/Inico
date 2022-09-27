#include <stdio.h>
#include <stdlib.h>
 
int main() {

    int num, cont_1;
    double n;

    while (scanf("%lf", &n) == 1)
    {
        cont_1 = 0;

        for (int i = 0; i < n; i++)
        {
            scanf("%d", &num);
            if (num == 1)
                cont_1++;
        }

        if (cont_1 >= 2*n/3)
            printf("impeachment\n");
        
        else
            printf("acusacao arquivada\n");
    }
 
    return 0;
}