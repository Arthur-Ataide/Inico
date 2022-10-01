#include "TAD Tarefa.h"

void inicializa(TAD_lista* tarefas){
    tarefas->fim = 0;
    tarefas->inicio = 0;
}

void inserir(TAD_lista* tarefas, char* novo){

    strcpy(tarefas->vetor_T[tarefas->fim].item, novo);
    tarefas->fim++;
}

int remover(TAD_lista* tarefas, int num){

    if (tarefas->fim == 0 || tarefas->fim < (num-1) || num < 0){
        printf("\nNao tem nenhum item nessa posicao.\n");
        return 1;
    }

    if (tarefas->fim == (num-1))
        tarefas->fim --;

    if (tarefas->fim > (num-1)){
        num--;
        for(int i = num; i < tarefas->fim; i++){
            strcpy(tarefas->vetor_T[i].item, tarefas->vetor_T[i+1].item);
        }

        tarefas->fim--;
    }

}

void imprimir(TAD_lista* tarefas){
    int cont = 0;

    for (cont = 0; cont < ((tarefas->fim)+1); cont++)
    {
        printf("\n%s\n", tarefas->vetor_T[cont].item);
    }
}

void intercalar(TAD_lista* tarefas1, TAD_lista* tarefas2, TAD_lista* tarefas3, int cont){

    for (int i = 0; i < cont; i++)
    {
        strcpy(tarefas3->vetor_T[tarefas3->fim].item, tarefas1->vetor_T[i].item);
        tarefas3->fim++;
        strcpy(tarefas3->vetor_T[tarefas3->fim].item, tarefas2->vetor_T[i].item);
        tarefas3->fim++;
    }

}


