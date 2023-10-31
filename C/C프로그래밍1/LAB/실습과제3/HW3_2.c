#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void) {
    int x, a = 0;
    printf("n값 입력: ");
    scanf("%d", &x);

    for (int i = 2; i < x; i++) {
        if (x % i == 0) {
            printf("소수가 아닙니다");
            a = 1;
            i = x;
        }
    }
    if (a != 1) {
        printf("소수입니다.");
    }

    return 0;
}