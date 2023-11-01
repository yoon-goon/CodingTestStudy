#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int c1=1,c2=2,c3=3,u1,u2,u3,strike,ball,trycnt = 0;
    srand(time(NULL));

    do {
        c1 = rand()%10;
        c2 = rand()%10;
        c3 = rand()%10;
    }   while (c1 == c2 || c2 == c3 || c1== c3);

    while(1){
        strike = 0, ball = 0;
        trycnt++;
        printf("%d %d %d\n",c1,c2,c3);
        printf("3숫자를 띄어쓰기로 구분해서 중복없이 입력하세요.(예시: 2 4 5)");
        scanf("%d %d %d",&u1,&u2,&u3);
        if(u1==c1) strike++;
        if(u2==c2) strike++;
        if(u3==c3) strike++;
        if(u1==c2||u1==c3) ball++;
        if(u2==c1||u2==c3) ball++;
        if(u3==c1||u3==c2) ball++;
        if(strike == 3){
            printf("3스트라이크 축하합니다!\n");
            printf("%d 시도",trycnt);
            break;
        }
        printf("%d스트라이크 %d볼\n",strike,ball);
    }
    return 0;
}