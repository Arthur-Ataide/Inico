#include <stdio.h>
#include <stdlib.h>

Tabuada(int, int);

int main()
{
    int N;

    scanf("%d", &N);
    Tabuada(1, N);

    return 0;
}

Tabuada(int x, int N)
{   
    printf("%d * %d = %d\n", x, N, x * N);
    x++;
    if (x != N + 1)
        Tabuada(x, N);

}
