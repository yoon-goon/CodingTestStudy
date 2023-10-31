#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main(void) {

	int x;
	printf("n값 입력: ");
	scanf("%d", &x);

	printf("약수: ");

	for (int i = 1; i <= x; i++) {
		if (x % i == 0) {
			printf("%d ", i);
		}
	}
	return 0;

}