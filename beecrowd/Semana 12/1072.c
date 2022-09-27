#include<stdio.h>

int main()
{

    int n, num, cont_in = 0, cont_out = 0;

    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num);
        if (num >= 10 && num <= 20)
            cont_in ++;
        else
            cont_out ++;

    }
    
    printf("%d in\n", cont_in);
    printf("%d out\n", cont_out);

    return 0;

}