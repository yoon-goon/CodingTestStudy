#include <stdio.h>
#include <stdlib.h>

#define SEAT 10
int main()
{
    int num;
    char inp;
    int arr[SEAT] = {0};
    while(1){
        inp=getchar();
        if (inp=='y'){
            printf("-----------------------\n1 2 3 4 5 6 7 8 9 10\n-----------------------\n");
            for(int i = 0;i<SEAT;i++){
                printf("%d ",arr[i]);
            }
        }
        else{
            break;
        }



    }


    return 0;
}
