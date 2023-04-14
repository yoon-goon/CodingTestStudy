#include <stdio.h>

int main()
{

        int a,b,i;


        scanf("%d",&a);
        scanf("%d",&b);//값 입력


        for(i=1; i < a && i < b; i++)//공약수기에 각각 숫자보다 클 수 없음
                if (a % i == 0 && b % i == 0) {// 공약수기에 두 조건 다 성립해야함
                    printf("%d ", i);
                }
        printf("\n");

        return 0;
}
