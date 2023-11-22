#include <stdio.h>
#include <stdlib.h>

#define SIZE 6
int main()
{

    int freq[SIZE] = {0};
    for(int i;i<10000;i++){
        ++freq[rand()%6];
    }

    printf("====================\n숫자 빈도\n====================\n");

    for(int i;i<SIZE;i++){
        printf("%d %3d\n",i+1,freq[i]);
    }


    return 0;
}
