#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
        srand(time(NULL));// 현재 시간을 seed로 설정
        for(int i = 0; i<4; i++){// 4번 연속 실행
                printf("%3d", rand() % 10);//padding 3  0과32767 사이 선택되는 수를 10으로 나눈 나머지를 출력
        }
        printf("\n");

        return 0;
}
