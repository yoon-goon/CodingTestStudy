#include <stdio.h>

int is_multiple(int n, int m){
    if(n%m==0){
        return 1;
    }
    else
        return 0;
}

int main(){
    int a,b;
    printf("첫번째 정수를 입력하시오: ");
    scanf("%d",&a);
    printf("두번째 정수를 입력하시오: ");
    scanf("%d",&b);

    if(is_multiple(a,b)==1)
        printf("%d는 %d의 배수입니다.",a,b);
    else
        printf("%d는 %d의 배수가 아닙니다.",a,b);

    return 0;
}