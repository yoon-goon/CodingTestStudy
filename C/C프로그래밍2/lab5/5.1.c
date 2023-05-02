#include <stdio.h>

int main(void)
{
        int a[] = {1,2,3,4,5};//배열 a 선언
        int *p = a;//포인터p는 배열 a의 첫 요소 가리킴
        int i;


        for(i=0;i<5;i++)
        {
                printf("%d",a[i]);//index를 이용한 출력
        }
        printf("\n");


        while (p < a+5)
        {
                printf("%d",*p);//포인터를 이용한 출력
                p++;
        }

	printf("\n");

        return 0;
}