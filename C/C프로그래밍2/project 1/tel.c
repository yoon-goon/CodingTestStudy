#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CONTACTS 100


struct Contact {
        char name[30];
        char phone[20];
        char memo[40];
};


int main() {
    char filename[] = "data.txt";
    FILE *file = fopen(filename, "a");

    if (file == NULL) {
        printf("파일을 열 수 없습니다.\n");
        return 1;
    }
}
    