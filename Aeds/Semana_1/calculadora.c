#include <stdio.h>
#include <stdlib.h>

void sum(int, int);
void menos(int, int);
void mult(int, int);

int main(){
    char ope;
    int num1, num2;

    scanf("%c %d %d", &ope, &num1, &num2);
    if(ope == '+')
        sum(num1, num2);

    else if(ope == '-')
        menos(num1, num2);

    else if(ope == '*')
        mult(num1, num2);
    
    return 0;
}

void sum(int a, int b){
    printf("%d", a + b);
}

void menos(int a, int b){
    printf("%d", a - b);
}

void mult(int a, int b){
    printf("%d", a * b);
}

