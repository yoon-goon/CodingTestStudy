#include <stdio.h>

int main(void)
{
        int a[][3] = {{1,2,3},{4,5,6},{7,8,9}};// 2차원배열 선언
        int *pa[] = {a[0],a[1],a[2]};// a의 1,2,3번째 요소의 시작주소
                                //포인터배열pa의 1,2,3에 할당
        int *p = a[0];// a의 첫요소 시작주소 포인터p에 할당

        int i;
        for (i = 0; i < 3; i++)
                printf("%d %d %d\n", a[i][2-i], *a[i], *(*(a+i)+i));
        putchar('\n');
        //a[i][2-i] 는 i값에 따라 해당 인덱스 값 출력
        //*a[i] = a[i][0], *(*(a+i)+i)) = a[i][i]


        for (i = 0; i<3; i++)
                printf("%d %d\n", *pa[i],p[i]);
        //*pa[i]는 pa[i]가 가리키는 주소에 저장된값 a[0],a[1],a[2]를 i에따라 출력
        //p[i]는 p가 가리키는 주소는 a[0]에서 i만큼 이동한 값과 같음
        putchar('\n');

        return 0;
}
