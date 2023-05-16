#include <stdio.h>

int main(void)
{
        struct node {
                int len;
                char* str;
        };

        struct node a[] = {5, "hello", 10, "world"};
        struct node *p = a; //포인터p가 a배열의 첫요소가리킴

        printf("a[0].len is %d\n", a[0].len);//첫요소 len 멤버값
        printf("p->len is %d\n", p->len);//p가 가리키는 구조체의 len 멤버값
        printf("p->str is %s\n", p->str);//p가 가리키는 구조체의 str 멤버값
        printf("*p++->str is %c\n", *p++->str);//p를 역참조후 한칸 이동
        printf("p->len is %d\n", p->len);//가리키는 위치 변경
        printf("p->str is %s\n", p->str);//가리키는 위치 변경

        return 0;
}
