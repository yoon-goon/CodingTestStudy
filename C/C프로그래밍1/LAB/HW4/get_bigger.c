#include <stdio.h>

double get_bigger(double n, double m);

int main()
{
    double a,b;
    printf("실수를 입력하시오: ");
    scanf("%lf %lf",&a,&b);
    get_bigger(a,b);

    return 0;
}

double get_bigger(double n, double m){
    if(n>m){
        printf("큰 수는 %.1lf입니다.",n);
    }
    else
        printf("큰 수는 %.1lf입니다.",m);
}