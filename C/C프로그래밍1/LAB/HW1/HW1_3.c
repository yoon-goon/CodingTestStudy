#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	double h;
	double w;
	double area;

	printf("삼각형의 밑변: ");
	scanf("%lf", &w);
	printf("삼각형의 높이: ");
	scanf("%lf", &h);


	area = h * w / 2;

	printf("삼각형의 넓이: %.2lf\n", area);

	return 0;
}