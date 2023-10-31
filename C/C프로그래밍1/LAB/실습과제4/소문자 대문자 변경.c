#include <stdio.h>

int main()
{
    char word;

    while (1)
    {
        printf("소문자를 입력하시오:");
        scanf(" %c",&word);

        if(word == 'Q')
            break;
        if (word >= 'a' && word <= 'z'){
            word -= 32;
            printf("변환된 대문자는 %c입니다.\n",word);
        }
        else
            continue;

    }

    return 0;
}