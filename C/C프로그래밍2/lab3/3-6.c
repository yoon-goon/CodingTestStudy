#include <stdio.h>

int main() {
    long a;
    int i,y;
    
    for (i=1;i<=20;i++){ // 1부터 20까지 계산
        a = 1;
        for (y=1;y<=i;y++){ // 1부터 i 까지 곱해서 a에 저장
            a *= y;
        }
        printf("%d! = %ld\n",i,a); //int 로 표현하기엔 너무 큰값
    }
    

    return 0;
}