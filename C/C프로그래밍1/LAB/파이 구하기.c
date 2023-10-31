#include <stdio.h>

int main()
{
    int num;
    double mom = 1.0, son = 4.0, pi = 0.0;
    printf("반복횟수:");
    scanf("%d",&num);

    while(num > 0){
        pi += son/mom;
        son *= -1;
        mom += 2.0;
        num -= 1;
    }
    printf("Pi = %f",pi);

    return 0;
}