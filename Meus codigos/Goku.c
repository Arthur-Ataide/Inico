#include <stdio.h>

int main(){
    int x, soma = 0;

    for (int i = 0; i < 10; i++)
    {   
        scanf("%d", &x);
        soma += x;
    }

    if (soma >= 8001)
        printf("Goku derrotou Freeza!\n");
    else
        printf("Freeza derrotou Goku!\n");

    return 0;

}