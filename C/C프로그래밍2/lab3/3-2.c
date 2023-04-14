#include <stdio.h>

int main() {
    int deci = 0;
	double backdot;
    char c;
    double a, b, rs;


    while ((c = getchar()) != EOF) { // EOF 전까지 계속 입력
        while (c == ' ') { // 첫 숫자 입력
            c = getchar();
        }
        if (c >= '0' && c <= '9') {
            a = c - '0'; //ascii 처리
            while ((c = getchar()) >= '0' && c <= '9') {
                a = a * 10 + (c - '0');
            }
            
            if (c == '.') { // 소수점 확인
                deci = 1; // 있을경우 출력형식을 double로 바꾸기위해 
                backdot = 0.1;
                while ((c = getchar()) >= '0' && c <= '9') { // 소수자리 처리
                    a += (c - '0') * backdot;
                    backdot *= 0.1; 
                }
            }
        }

        while (c == ' ') {
            c = getchar();
        }
        if (c == '+' || c == '-' || c == '*' || c == '/' || c == '%') { // 연산자 확인
            char oper = c;
            c = getchar();
            while (c == ' ') {
                c = getchar();
            }
            if (c >= '0' && c <= '9') { // c 에 숫자가 들어왔을 경우
                b = c - '0'; //ascii 처리
                while ((c = getchar()) >= '0' && c <= '9') {
                    b = b * 10 + (c - '0'); // 자릿수 처리
                }
                if (c == '.') { // 소수점 확인
                    backdot = 0.1;
                    while ((c = getchar()) >= '0' && c <= '9') {
                        b += (c - '0') * backdot;
                        backdot *= 0.1;
                    }
                }
            }

            // operator case 구분
            switch (oper) {
                case '+':
                    rs = a + b;
                    break;
                case '-':
                    rs = a - b;
                    break;
                case '*':
                    rs = a * b;
                    break;
                case '/':
                    rs = a / b;
                    break;
                case '%':
                    rs = (int)a % (int)b;
                    break;
                default: // 해당되지 않을경우 잘못된 연산자임을 출력
                    printf("잘못된 opererator\n");
                    continue;
            }

            // 결과 출력
            if (deci == 0){ // 소수점이 없었으면 int형식 출력
                printf("%d\n",(int)rs);
            }
            else{ //변수에 소수점이 있었으면
                printf("%.6f\n", rs);
            }

            // 초기화
            deci = 0;
            a = rs;
        }
    }

    return 0;
}

