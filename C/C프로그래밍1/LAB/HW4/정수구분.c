#include <stdio.h>

int even(int n);
int absolute(int n);
int sign(int n);

int main()
{
    int a;
    printf("정수를 입력하시오: ");
    scanf("%d",&a);

    printf("even()의 결과: %d\n", even(a));
    absolute(a);
    printf("sign()의 결과: %d\n", sign(a));

    return 0;
}



int even(int n){
    if(n%2==0)
        return 1;
    else
        return 0;
}

int absolute(int n){
    if(n<0)
        printf("absolute()의 결과: %d\n",n*-1);
    else
        printf("absolute()의 결과: %d\n",n);
}

int sign(int n){
    if(n<0)
        return -1;
    else if(n==0)
        return 0;
    else
        return 1;
}