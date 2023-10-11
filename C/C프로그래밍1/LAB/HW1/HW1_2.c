#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	double mile;
	double mt;

	printf("마일을 입력하시오.: ");
	scanf("%lf", &mile);

	mt = mile * 1609;

	printf("%.1lf 마일은 %.2lf미터입니다.\n", mile, mt);

	return 0;
}