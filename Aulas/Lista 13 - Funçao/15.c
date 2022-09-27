#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int dist(int, int, int, int, int, int);

int main()
{
    int x1, y1, x2, y2, z1, z2;
    scanf("%d %d %d %d %d %d", &x1, &y1, &z1, &x2, &y2, &z2);
    printf("%d", dist(x1, y1, z1, x2, y2, z2));
    return 0;
}

int media(int x1, int y1, int z1, int x2, int y2, int z2)
{   
    return sqrt(pow(x2-x1,2) + pow(y2-y1, 2) + pow(z2-z1, 2));
}
