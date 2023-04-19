#include <stdio.h>

char my_strcpy(char *dest, char *source) {//문자열 복사
    char *tmp = dest;
    while ((*dest++ = *source++) != '\0');
    return *tmp;
}


int my_strcmp(char *s, char *t)//문자열 비교
{
        for (int i=0;s[i] == t[i]; i++)
                if (s[i] == '\0')
                        return 0;
        return *s - *t;
}

void sort(char arr[][10], int left, int right) {
    if (left >= right) {//탈출 조건
        return;
    }
    char pivot[10];//NAMELEN이 10이므로 pivot도 최대 10자
    my_strcpy(pivot, arr[(left+right)/2]);//중간위치 pivot 설정
    int i = left, j = right;
    while (i <= j) {
        while (my_strcmp(arr[i], pivot) < 0) {//피봇보다 작은경우
            i++;
        }
        while (my_strcmp(arr[j], pivot) > 0) {//피봇보다 큰 경우
            j--;
        }
        if (i <= j) {// temp를 이용해서 두 요소 변경
            char temp[10];
            my_strcpy(temp, arr[i]);
            my_strcpy(arr[i], arr[j]);
            my_strcpy(arr[j], temp);
            i++;
            j--;
        }
    }
    sort(arr, left, j);//재귀
    sort(arr, i, right);
}


#define ELEMENTS 7
#define NAMELEN 10

int main(void)
{

        char array[ELEMENTS][NAMELEN] = {"kim", "lee", "park", "choi", "jung", "kang", "cho"};
        //배열 초기화
         for (int i = 0; i < ELEMENTS; i++) {// 정렬 전 출력
            printf("%s ", array[i]);
        }
        printf("\n");

        sort(array, 0, ELEMENTS-1);//9 값으로는 배열의 크기를 넘어 에러가 발생 배열에 맞춘 값으로 수정

         for (int i = 0; i < ELEMENTS; i++) {//정렬 후 출력
            printf("%s ", array[i]);
        }
        printf("\n");

        return 0;
}



