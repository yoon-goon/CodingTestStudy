#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
    return strcmp(*(const char**)a, *(const char**)b);// 앞뒤 비교
}

int main(int argc, char *argv[]) {
    int r = 0; // -r input 처리
    if (argc > 1 && strcmp(argv[1], "-r") == 0) {// -r 처리
        r = 1;
        argc--;
        argv++;
    }

    qsort(argv+1, argc-1, sizeof(char*), compare);//소트과정
    if (r) {
        for (int i = argc-1; i >= 1; i--) {
            printf("%s ", argv[i]);
        }
    } else {
        for (int i = 1; i < argc; i++) {
            printf("%s ", argv[i]);
        }
    }
    putchar('\n');

    return 0;
}

