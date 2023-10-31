#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int x, sum = 0;
	printf("n값 입력: ");
	scanf("%d", &x);

	while (x > 0) {
		sum += x % 10;
		x = x / 10;
		//printf("%d %d ",sum,x);
	}

	printf("각 자리수의 합: %d", sum);

	return 0;
}