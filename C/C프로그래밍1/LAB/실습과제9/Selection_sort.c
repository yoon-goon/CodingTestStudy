#include <stdio.h>
#define SIZE 10

int main()
{
    int lst[SIZE] = {3,2,9,7,1,4,8,0,6,5};
    int i,j,tmp,least;

    for(i=0;i<SIZE-1;i++){
        least = i;
        for(j = i + 1;j<SIZE;j++){ // i + 1 : 이미 정렬된 부분을 제외하고 검사
            if(lst[j]<lst[least])
                least = j;
        }

        tmp = lst[i];
        lst[i]=lst[least];
        lst[least] = tmp;
    }

    for(i = 0;i<SIZE;i++){
        printf("%d ",lst[i]);
    }

    return 0;
}
