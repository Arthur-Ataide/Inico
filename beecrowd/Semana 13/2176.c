#include <stdio.h>
#include <stdlib.h>

int main(){
    char S[100];
    int tamanho, cont_1 = 0;

    scanf("%s", &S);
    tamanho = strlen(S);

    for (int i = 0; i < tamanho; i++)
    {
        if (S[i] == '1')
            cont_1++;
    }
    
    if (cont_1 % 2 != 0)
        printf("%s1\n", S);
    else 
        printf("%s0\n", S);

    return 0;
}