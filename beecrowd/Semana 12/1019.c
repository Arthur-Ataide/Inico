#include<stdio.h>

int main()
{

    int n, tempo[3];
    int transf[3] = {3600, 60, 1};
    scanf("%d", &n);

    for (int i = 0; i < 3; i++)
    {
        tempo[i] = n/transf[i];
        n = n % transf[i];
    }
    
    printf("%d:%d:%d\n", tempo[0], tempo[1], tempo[2]);

    return 0;

}