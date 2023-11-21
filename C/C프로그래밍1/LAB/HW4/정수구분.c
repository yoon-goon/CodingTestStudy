#include <stdio.h>

int even(int n){
    if(n%2==1)
        return 1;
    else
        return 0;
}

int absolute(int n){
    if(n<0)
        printf("absolute()의 결과: %d",n*-1);
    else
        printf("absolute()의 결과: %d",n);
}

int main()
{
    int a = 14;
    printf("%d\n", even(a));
    absolute(a);

    return 0;
}