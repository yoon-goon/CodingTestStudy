#include <stdio.h>
#include <string.h>

int mystrlen(char *s){
        int n;
        for(n=0;*s != '\0'; s++)// '\0' = NULL , 문자열의 끝까지
                n++;
        return n;// 길이 반환
}

int main(void)
{
        char *s[] = {"This is Lab5", "Easy C Programming", "Have fun"};

        printf("with strlen()\n");
        int n = (int)(sizeof(s)/sizeof(char *));
        // 자료형의 크기로 나눠 배열의 크기 구함
        for (int i = 0; i < n; i++)
                printf("%s %d\n",*(s+i),(int)strlen(s[i])); //*(s+i) == s[i]
        putchar('\n');

        for (int i=0;i<n;i++)
                printf("%s %d\n",*(s+i),(int)mystrlen(s[i])); //*(s+i) == s[i]
        putchar('\n');
}
