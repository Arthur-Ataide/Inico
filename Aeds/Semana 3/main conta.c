#include "conta.c"
#include "Cliente.c"

int main(){
    Conta conta1;
    Cliente pessoa1;
    char nome[15], CPF[20], tipo[20], ende[50];
    int ano;
    double saldo, dep, saq;

    printf("Qual seu nome? \n");
    scanf("%s", &nome);

    printf("Qual seu CPF? \n");
    scanf("%s", &CPF);

    printf("Qual seu Endereco? \n");
    scanf("%s", &ende);

    printf("Qual o tipo da sua conta? \n");
    scanf("%s", &tipo);

    printf("Qual o ano da sua conta? \n");
    scanf("%d", &ano);

    printf("Qual o saldo atual? \n");
    scanf("%lf", &saldo);

    printf("Vai depositar quanto? \n");
    scanf("%lf", &dep);

    printf("Vai sacar quanto? \n");
    scanf("%lf", &saq);


    inciacao (&conta1, tipo, ano, saldo);
    iniciar_cliente(&pessoa1, ende, nome, CPF);
    deposito(&conta1, dep);
    saque(&conta1, saq);
    avaliacao(&conta1, conta1.ano);
    saida(pessoa1);
    imprime(conta1);

    return 0;
}
