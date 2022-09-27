#include <stdio.h>
#include <stdlib.h>

float opera(float, float, char);

int main()
{
    float a, b;
    char op;
    scanf("%f %f %c", &a, &b, &op);
    printf("%f", opera(a, b, op));
    return 0;
}

float opera(float a, float b, char op)
{   
    int result;
    if (op == "/")
        result = a / b;
    if (op == "-")
        result = a - b;
    if (op == "+")
        result = a + b;
    if (op == "*")
        result = a * b;
    return result;
}
