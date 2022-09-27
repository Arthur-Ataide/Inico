#include <stdio.h>
#include <stdlib.h>

int pe(int);

int main()
{
    int pol;
    scanf("%d", &pol);
    printf("%d", pe(pol));
    return 0;
}

int pe(int x)
{   
    x = x/12;
    return x;
}
