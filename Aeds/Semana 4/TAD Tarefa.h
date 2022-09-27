#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct{
    char item[100];
}TAD_tarefa;


typedef struct{
    
    TAD_tarefa vetor_T[100];
    int inicio, fim;

}TAD_lista;

void inicializa(TAD_lista* tarefas);
void inserir(TAD_lista* tarefas, char* novo);
int remover(TAD_lista* tarefas, int num);
void imprimir(TAD_lista* tarefas);

