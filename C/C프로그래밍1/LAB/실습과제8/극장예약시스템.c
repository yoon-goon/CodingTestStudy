#include <stdio.h>
#include <stdlib.h>

#define SEAT 10
int main()
{
    int num;
    char inp;
    int arr[SEAT] = {0};

    while(1){
        printf("좌석을 예약하시겠습니까?(y또는n): ");
        scanf(" %c",&inp);
        if(inp=='y'){
            printf("-----------------------\n1 2 3 4 5 6 7 8 9 10\n-----------------------\n");
            for(int i = 0;i<SEAT;i++){
                printf("%d ",arr[i]);
            }

            printf("\n몇번째 좌석을 예약하시겠습니까? ");
            scanf("%d",&num);
            
            if (arr[num-1] == 0){
                arr[num-1] = 1;
                printf("예약되었습니다.\n");
            }
            else
                printf("이미 예약된 자리입니다.\n");
        }
        else if(inp=='n'){
            break;
        }
    }
    return 0;
}
