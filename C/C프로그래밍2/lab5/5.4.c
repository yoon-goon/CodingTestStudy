#include <stdio.h>

void b(int *p)
{
        printf("%d %d %d\n", p[0],p[-1],p[-2]);
        return;
}

int main(void)
{
        int a[] = {0,1,2,3,4,5,6,7,8,9};//배열 a 선언

        int n = (int)(sizeof(a)/sizeof(int));//n = 배열 a의 크기
        for(int i = 0; i<n;i++)
                printf("%d ", a[i]);// 배열의 끝까지 출력
        putchar('\n');

        b(a+n-1);//a배열의 마지막을 가리키는 포인터
        // 그러므로 p[0], p[-1], p[-2]는 마지막원소부터 앞쪽으로 2개

        return 0;
}
