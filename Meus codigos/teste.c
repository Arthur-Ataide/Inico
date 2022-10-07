#include <stdio.h>
#include<stdlib.h>
 
int main() {
 
    int a, maiorQ, menorQ;
    char v[1003];
    
    scanf("%d", &a);
    maiorQ = 0;
    menorQ = 0;
    for(int i = 0; i < a; i++){
        scanf("%s", v);
        for(int j = 0; j < strlen(v); j++){
            if (v[j] == '<')
                menorQ += 1;
            
            if (v[j] == '>')
                maiorQ += 1;
        }
    
    if(maiorQ > menorQ)
        printf("%d\n", menorQ);
    else 
        printf("%d\n", maiorQ);
    }
    
 
    return 0;
}