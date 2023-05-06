#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) { // echo 구현
    int i;
    if (argc > 1 && strcmp(argv[1], "-r")==0){ // -r 입력
        for (i = argc-1; i >= 2;i--){
            printf("%s%s", argv[i], (i < argc) ? " " : "");// 문자 사이 공백
        }
    }
    else{ // -r 이 입력되지 않았을경우
        for (i = 1; i < argc; i++)
            printf("%s%s", argv[i], (i < argc-1) ? " " : "");
    }
    printf("\n");
    return 0;
}
