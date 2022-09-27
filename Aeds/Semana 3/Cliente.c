#include "Cliente.h"

void iniciar_cliente(Cliente* pessoa, char* ende, char* nome, char* CPF){
    strcpy(pessoa->ende, ende);
    strcpy(pessoa->nome, nome);
    strcpy(pessoa->CPF, CPF);
}

void saida(Cliente pessoa){
    printf("\n\n\nNome = %s\n", pessoa.nome);
    printf("CPF = %s\n", pessoa.CPF);
    printf("Endereco = %s\n", pessoa.ende);
}
