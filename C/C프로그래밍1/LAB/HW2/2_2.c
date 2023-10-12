#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>


int main(void) {

	int x = 50, y = 50, z = 30, a, b, c;
	printf("x,y좌표값과 반지름을 입력하세요(띄어쓰기로구분): ");
	scanf("%d %d %d", &a, &b, &c);

	double distance = sqrt((a - x) * (a - x) + (b - y) * (b - y));

	printf("%lf", distance);

	if (distance + c <= z) {
		printf("A가 B를 포함합니다.");
	}
	else if (distance + z <= c) {
		printf("B가 A를 포함합니다.");
	}
	else if (distance < z + c) {
		printf("A와 B가 부분적으로 겹칩니다.");
	}
	else
		printf("A와 B가 겹치지 않습니다.");

	return 0;

}