#include <stdio.h>
#include <stdlib.h>

int C(int);

int main()
{
    int f;
    scanf("%d", &f);
    printf("%f", C(f));
    return 0;
}

int C(int f)
{   float c;
    c = (f - 32) * 1.8;
    return c;
}
