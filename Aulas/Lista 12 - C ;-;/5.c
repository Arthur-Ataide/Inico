#include <stdio.h>
#include <stdlib.h>
int main(){
    for (int i = 0; i < 501; i++)
    {
        if(i % 5 == 0)
            printf("%d\n", i);
    }

    return 0;
}
