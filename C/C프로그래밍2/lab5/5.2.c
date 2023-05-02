#include <stdio.h>

int main(void)
{
	int a[][3] = {{1,2,3},{4,5,6},{7,8,9}};// 2차원배열 선언
	int *pa[] = {a[0],a[1],a[2]};// a의 1,2,3번째 요소를
				//포인터배열pa의 1,2,3에 할당
	int *p = a[0];// a의 1요소 시작주소 포인터p에 할당

	int i;
	for (i = 0; i < 3; i++)
		printf("%d %d %d\n", a[i][2-i], *a[i], *(*(a+i)+i));
	putchar('\n');
	//a[i][2-i] 는 i값에 따라 해당 인덱스 값 출력
	//


	for (i = 0; i<3; i++)
		printf("%d %d\n", *pa[i],p[i]);
	putchar('\n');

	return 0;
}