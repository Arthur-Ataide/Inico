#include "TAD Tarefa.c"

int main(){

    TAD_lista tarefas1, tarefas2, tarefas3;
    char novo[100];
    int tirar, cont;

     inicializa(&tarefas1);
     inicializa(&tarefas2);
     inicializa(&tarefas3);

     printf("Quer colocar quantas tarefas na lista?\n");
     scanf("%d", &cont);

    for (int i = 0; i < cont ; i++)
    {
        printf("Qual tarefa voce quer adicionar?\n");
        scanf("%s", &novo);
        inserir(&tarefas1, novo);
    }

    printf("Proxima lista\n");

    for (int i = 0; i < cont ; i++)
    {
        printf("Qual tarefa voce quer adicionar?\n");
        scanf("%s", &novo);
        inserir(&tarefas2, novo);
    }
    
    intercalar(&tarefas1, &tarefas2, &tarefas3, cont);
    

    printf("Qual posicao da lista sera tirada?\n");
    scanf("%d", &tirar);

    remover(&tarefas3, tirar);
    imprimir(&tarefas3);

    return 0;
}
