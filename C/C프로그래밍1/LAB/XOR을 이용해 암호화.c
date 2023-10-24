#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    char data = 'a';
    char key = 0xff;
    char enc,ori;

    printf("원래의 문자=%c\n",data);

    enc = data ^ key;
    printf("암호화된 문자 = %c\n",enc);

    ori = enc ^ key;
    printf("복호화된 문자 = %c\n",ori);
    
    return 0;

}