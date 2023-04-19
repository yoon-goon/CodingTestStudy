#include <stdio.h>

char my_strcpy(char *dest, char *source) {
    char *tmp = dest;
    while ((*dest++ = *source++) != '\0');
    return tmp;
}


int my_strcmp(char *s, char *t)
{
        for (int i=0;s[i] == t[i]; i++)
                if (s[i] == '\0')
                        return 0;
        return *s - *t;
}

void sort(char arr[][10], int left, int right) {
    if (left >= right) {
        return;
    }
    char pivot[10];
    my_strcpy(pivot, arr[(left+right)/2]);
    int i = left, j = right;
    while (i <= j) {
        while (my_strcmp(arr[i], pivot) < 0) {
            i++;
        }
        while (my_strcmp(arr[j], pivot) > 0) {
            j--;
        }
        if (i <= j) {
            char temp[10];
            my_strcpy(temp, arr[i]);
            my_strcpy(arr[i], arr[j]);
            my_strcpy(arr[j], temp);
            i++;
            j--;
        }
    }
    sort(arr, left, j);
    sort(arr, i, right);
}

#define ELEMENTS 7
#define NAMELEN 10





int main(void)
{

        char array[ELEMENTS][NAMELEN] = {"kim", "lee", "park", " choi", "jung", "kang", "cho"};

         for (int i = 0; i < ELEMENTS; i++) {
            printf("%s ", array[i]);
        }
        printf("\n");

        sort(array, 0, ELEMENTS-1);

         for (int i = 0; i < ELEMENTS; i++) {
            printf("%s ", array[i]);
        }
        printf("\n");

        return 0;
}
