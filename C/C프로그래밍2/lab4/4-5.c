#include <stdio.h>
int i = 10;// i선언 10으로 초기화

void f(void)
{
        printf("i in f() is %d\n", i++);//출력후 1 증가
}

void s(void)
{
        static int i = 100;//정적변수 i 선언 100초기화
        printf("i in s() is %d\n", i++);//i 출력후 1증가
}

int main(void)
{
        for ( int j = 0; j < 3; ++j)//3회 실행
        {
                printf("i in main() is %d\n", i++);//전역변수 i의 값 출력, 1증가
                f();//함수호출
                s();
        }
        return 0;
}
