#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_Contacts 100

struct Contact {
        char name[30];
        char phone[20];
        char memo[40];
};


int main(int argc, char *argv[]) {
    if (argc < 4 || argc > 5) {
        printf("잘못된 명령어입니다. 사용법: ./tel -a 이름 전화번호 메모(옵션)\n");
        return 1;
    }

    if (strcmp(argv[1], "-a") != 0) { // 다른 명령도 수행하도록 수정해야함
        printf("잘못된 옵션입니다. -a 옵션을 사용하세요.\n");
        return 1;
    }

    char filename[] = "data.txt";
    FILE *file = fopen(filename, "a");

    if (file == NULL) {
        printf("파일을 열 수 없습니다.\n");
        return 1;
    }
	
	if (argc != 5) {
		argv[4] = "";
	}
	
	printf("%s %s %s\n", argv[2], argv[3], argv[4]);

    // 파일에 추가할 내용을 문자열로 생성
    char entry[MAX_Contacts];
    snprintf(entry, MAX_Contacts, "%s:%s:%s\n", argv[2], argv[3], argv[4]);

    // 파일에 내용 추가
    fputs(entry, file);

    printf("data.txt 파일에 추가되었습니다.\n");

    fclose(file);

    return 0;
}
