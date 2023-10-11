#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	double earning;
	double years;

	printf("연봉을 입력하시오: ");
	scanf("%lf", &earning);


	years = 100000 / earning;

	printf("10억을 모으는데 걸리는 시간(단위: 년): %.2lf\n", years);

	return 0;
}