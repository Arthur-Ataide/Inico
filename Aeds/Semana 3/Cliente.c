#include "Cliente.h"

void iniciar_cliente(Cliente* pessoa, char* ende, char* nome, char* CPF){
    strcpy(pessoa->ende, ende);
    strcpy(pessoa->nome, nome);
    strcpy(pessoa->CPF, CPF);
}

void saida(Cliente pessoa){
    printf("\n\n\n\nNome = %s\n", pessoa.nome);
    printf("CPF = %s\n", pessoa.CPF);
    printf("Endereco = %s\n", pessoa.ende);
}

void alocar(Cliente ** pessoas, Conta ** contas, int num, int cont){

    

    if(cont == 0){
        (*contas) = (Conta*) malloc(sizeof(Conta) * num);
        (*pessoas) = (Cliente*) malloc(sizeof(Cliente) * num);
    }
    else 
    {      
        Cliente * guard1 = &contas;
        Conta * guard2 = &pessoas;

        (*contas) = (Conta*) realloc((Conta*) *contas, sizeof(Conta) * num);
        (*pessoas) = (Cliente*) realloc((Cliente*) *pessoas, sizeof(Cliente) * num);

        free(guard1);
        free(guard2);
    }
}
