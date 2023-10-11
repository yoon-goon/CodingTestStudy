#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	double f;
	double c;

	printf("화씨값을 입력하시오: ");
	scanf("%lf", &f);

	c = 5.0 / 9 * (f - 32);

	printf("섭씨값은: %.2lf도 입니다.\n", c);

	return 0;
}