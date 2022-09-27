#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char tipo[20], avaliacao[15];
    double saldo;
    int ano;
} Conta;

void inciacao(Conta* conta, char* tipo, int ano, double saldo);
void deposito(Conta* conta, double dep);
void saque(Conta* conta, double saq);
void avaliacao(Conta* conta, int ano);
void imprime(Conta conta);
