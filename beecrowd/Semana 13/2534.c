#include <stdio.h>
 
int main() {
    
    int n, q, p, valor, aux;
    while (scanf("%d %d", &n, &q) != EOF)
    {

        int notas[n], posicao[q];
        
        for (int i = 0; i < n; i++)
            scanf("%d", &notas[i]);

        valor = 1;

        while (valor == 1)
        {
            valor = 0;

            for (int i = 0; i < n-1; i++)
            {
                if (notas[i] < notas[i+1])
                    {
                        aux = notas[i];
                        notas[i] = notas[i+1];
                        notas[i+1] = aux;
                        valor = 1;

                    }
            }
            
        }

        for (int i = 0; i < q; i++)
            scanf("%d", &posicao[i]);
        
        for (int i = 0; i < q; i++)
        {
            printf("%d\n", notas[posicao[i]-1]);
        }
    
    }
 
    return 0;
}