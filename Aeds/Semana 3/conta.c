#include "conta.h"

void inciacao(Conta* conta, char* tipo, int ano, double saldo){
    conta->ano = ano;
    strcpy(conta->tipo, tipo);
    conta->saldo = saldo;
}

void deposito(Conta* conta, double dep){
    conta->saldo += dep;
}

void saque(Conta* conta, double saq){
    conta->saldo -= saq;
}

void avaliacao(Conta* conta, int ano){
    if (conta-> ano <= 2017)
        strcpy(conta->avaliacao, "Valido");
    else
        strcpy(conta->avaliacao, "Invalido");
}

void imprime(Conta conta){
    printf("Tipo = %s\n", conta.tipo);
    printf("Ano = %d\n", conta.ano);
    printf("Saldo = %.2lf\n", conta.saldo);
    printf("Emprestimo = %s\n", conta.avaliacao);
}
