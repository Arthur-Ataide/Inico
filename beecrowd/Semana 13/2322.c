#include <stdio.h>
 #include <stdlib.h>

int main() {
 
    int n, num, *cont, sequencia = 0;

    scanf("%d", &n);
    cont = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        cont[i] = 0;
    }

    for (int i = 1; i < n; i++)
    {
        scanf("%d", &num);
        cont[num-1]++;
    }

    for (int i = 0; i < n; i++)
    {
        if (cont[i] == 0)
            printf("%d\n", i+1);
    }
    
    return 0;

}