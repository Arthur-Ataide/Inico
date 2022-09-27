#include <stdio.h>
#include <stdlib.h>

int Fibonacci(int);

int main()
{
    int x;

    scanf("%d", &x);
    printf("%d",Fibonacci(x));

    return 0;
}

int Fibonacci(int x)
{   
    int fib;

    if (x == 1 || x == 2)
        return 1;
    
    fib = Fibonacci(x-1) + Fibonacci(x-2);
    return fib;
}
