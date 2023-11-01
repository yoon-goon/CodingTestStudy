#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int inp,cpu;
    srand(time(NULL));

    while (1){
        printf("1~3의 숫자를 입력하세요.(1은 가위, 2는 바위, 3은 보, 4를 입력해 종료)");
        scanf("%d",&inp);
        cpu = rand()%3+1;
        if(inp == 4){
            break;
        }
        switch(cpu){
            case 1:
            printf("컴퓨터는 가위를 냈습니다.\n");
            break;
            case 2:
            printf("컴퓨터는  바위를 냈습니다.\n");
            break;
            case 3:
            printf("컴퓨터는 보를 냈습니다.\n");
            break;
        }

        if(inp == cpu){
            printf("비겼습니다.\n");
        }
        else if ((inp == 1 && cpu == 3) ||
                   (inp == 2 && cpu == 1) ||
                   (inp == 3 && cpu == 2)) {
            printf("사용자가 이겼습니다!\n");
        }
        else
        {
            printf("컴퓨터가 이겼습니다!\n");
        }
    }
    return 0;
}