#include <stdio.h>
#include <stdlib.h>

int seg(int, int, int);

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d", seg(a, b, c));
    return 0;
}

int seg(int a, int b, int c)
{   
    return (a*60*60)+b*60+c;
}
