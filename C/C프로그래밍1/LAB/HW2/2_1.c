#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int a, b, c;

	printf("세 변의 길이를 입력하세요(띄어쓰기로 구분): ");
	scanf("%d %d %d", &a, &b, &c);


	if (a + b > c && b + c > a && a + c > b) {
		if (a == b && b == c) {
			printf("정삼각형");
		}
		else if (a * a + b * b == c * c || a * a + c * c == b * b || b * b + c * c == a * a) {
			printf("직각삼각형");
		}
		else if (a == b || a == c || b == c) {
			printf("이등변삼각형");
		}
		else
			printf("일반삼각형");
	}
	else
		printf("삼각형이 될 수 없음");

	return 0;
}