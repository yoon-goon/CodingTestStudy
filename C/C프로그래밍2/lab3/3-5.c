#include <stdio.h>

int main() {
    int b,i,y;

    for(i=2;i<=200;i++){ //1은 소수가 아니므로 2부터
        b = 0;
        for (y=2;y<i;y++){ // 1과 자신을 제외한 숫자로 나눠진다면 소수가 아니기 떄문에
            if (i % y == 0)
            {
                b = 1;
                continue;// 나눠졌을 경우 다음 y부터 이어서 실행
            }
        }
        if (b == 0){
            printf("%d ",i);
        }
        }
    printf("\n");
    return 0;
}
