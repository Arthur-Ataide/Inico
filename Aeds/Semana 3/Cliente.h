#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nome[15], CPF[20], ende[100];
} Cliente;

void iniciar_cliente(Cliente* pessoa, char* ende, char* nome, char* CPF);
void saida(Cliente pessoa);