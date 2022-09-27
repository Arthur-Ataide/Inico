#include "TAD Tarefa.c"

int main(){

    TAD_lista tarefas;
    char novo[100];
    int tirar, cont;

     inicializa(&tarefas);

     printf("Quer colocar quantas tarefas na lista?\n");
     scanf("%d", &cont);

    for (int i = 0; i < cont ; i++)
    {
        printf("Qual tarefa voce quer adicionar?\n");
        scanf("%s", &novo);
        inserir(&tarefas, novo);
    }
    
    

    printf("Qual posicao da lista sera tirada?\n");
    scanf("%d", &tirar);

    remover(&tarefas, tirar);
    imprimir(&tarefas);



    return 0;
}
