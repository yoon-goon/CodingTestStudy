#include <stdio.h>

int factorial(int n){
    int result = 1;

    for(int i=1;i<=n;i++)
        result *= i;
    return result;
}

int combination(int n, int r){
    return (factorial(n)/(factorial(n-r)*factorial(r)));
}

int get_integer(void){
    int n;
    printf("정수를 입력하세요:");
    scanf("%d",&n);
    return n;
}

int main(void){
    int a,b;
    a = get_integer();
    b = get_integer();
    printf("C(%d,%d) = %d \n",a,b,combination(a,b));

    return 0;
}