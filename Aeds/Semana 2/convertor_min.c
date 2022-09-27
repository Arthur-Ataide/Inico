#include <stdio.h>

typedef struct
{
    int h, m;
}Tempo;

void hm(int, Tempo*);

int main(){
    int mnts;
    Tempo temp;
    Tempo *hora = NULL;
    hora = &temp;

    scanf("%d", &mnts);

    hm(mnts, hora);

    printf("%d horas\n%d minutos", temp.h, temp.m );
    
    return 0;
}

void hm(int mnts, Tempo *hora){

    hora -> h = mnts / 60;
    hora -> m = mnts - (hora -> h * 60);
}

