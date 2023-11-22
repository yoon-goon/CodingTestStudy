#include <stdio.h>

void check_alpha(char c);

int main()
{
    char a;
    printf("문자를 입력하세요: ");
    a = getchar();
    check_alpha(a);

    return 0;
}

void check_alpha(char c){
    if (c>='A' && c<='z')
        printf("%c는 알파벳 문자입니다.",c);
    else
        printf("%c는 알파벳 문자가 아닙니다.",c);
}