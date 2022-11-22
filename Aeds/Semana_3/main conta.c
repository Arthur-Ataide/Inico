#include "conta.c"
#include "Cliente.c"

int main(){
    Conta *contas;
    Cliente *pessoas;
    char nome[15], CPF[20], tipo[20], ende[50];
    int ano, continuar, num, cont;
    double saldo, dep, saq;

    continuar = 1;
    cont = 0;

    while (continuar)
    {
        printf("\n\nQuantos clientes vao ser adicionados?\n");
        scanf("%d", &num);
    
        alocar(&pessoas, &contas, num, cont);


        for(int i = cont; i < cont + num; i++){
    
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


            inciacao (&contas[i], tipo, ano, saldo);
            iniciar_cliente(&pessoas[i], ende, nome, CPF);
            deposito(&contas[i], dep);
            saque(&contas[i], saq);
            avaliacao(&contas[i], contas[i].ano);
            saida(pessoas[i]);
            imprime(contas[i]);

        }
        printf("Deseja adicionar mais clientes? Se sim digite 1 se nao digite 0: ");
        scanf("%d", &continuar);

        cont =+ num;
    }

    for(int i = 0; i < cont; i++){
        saida(pessoas[i]);
        imprime(contas[i]);
    }

    return 0;
}
