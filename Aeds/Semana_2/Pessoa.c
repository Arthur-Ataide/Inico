# include <stdio.h>

typedef struct
{
    char nome[20], data[15], CPF[15];
}Pessoa;

void recebimento (Pessoa*);

int main(){
    Pessoa p;
    Pessoa *indv = &p;

    recebimento(indv);

    printf("nome = %s\ndata = %s\nCPF = %s", indv -> nome, indv -> data, indv -> CPF);

    return 0;
}

void recebimento(Pessoa *indv){
    scanf("%s %s %s", indv->nome, indv->data, indv->CPF);
}
