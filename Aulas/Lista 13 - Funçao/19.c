#include <stdio.h>
#include <stdlib.h>
int soma(char);
int main(){
    char num[15];
    for (int i = 0; i < 15; i++)
        scanf("%d", num[i]);
    printf("%d", soma(num));
    return 0;
}
int soma(char num)
{
    int S = 0;
   for (int i = 0; i < 15; i++)
    {
        S+= num[i];
    } 
    return S;

}
