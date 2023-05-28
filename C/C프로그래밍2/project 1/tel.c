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
    if (argc != 2 && (argc < 4 || argc > 5)) {
        printf("잘못된 명령어입니다. 사용법: ./tel -a 이름 전화번호 메모(옵션)\n");
        return 1;
    }

    if (strcmp(argv[1], "-a") == 0) {
        if (argc < 4 || argc > 5) {
            printf("-a 옵션을 사용할 때는 이름, 전화번호, 메모(필수아님)를 입력하세요.\n");
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
		
		printf("add? [Y/N]: ");
		char answer;
		scanf(" %c", &answer);	
	
		if (answer == 'Y' || answer == 'y') {
			// 파일에 추가할 내용을 문자열로 생성
			char entry[MAX_Contacts];
			snprintf(entry, MAX_Contacts, "%s:%s:%s\n", argv[2], argv[3], argv[4]);
	
			// 파일에 내용 추가
			fputs(entry, file);
	
			printf("data.txt 파일에 추가되었습니다.\n");
		}
		else {
			printf("저장하지 않고 프로그램을 종료합니다.\n");
		}

    fclose(file);
	}
	else{
		// search 구현
		char number[20];
        strcpy(number, argv[1]);

        char filename[] = "data.txt";
        FILE *file = fopen(filename, "r");

        if (file == NULL) {
            printf("파일을 열 수 없습니다.\n");
            return 1;
        }

        char line[MAX_Contacts];
        int found = 0;
		int order = 1;

        while (fgets(line, sizeof(line), file) != NULL) {
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");
			

            if (strstr(phone, number) != NULL) {
                printf("%d %s %s %s\n", order, name, phone, memo);
                found = 1;
				order += 1;
            }
			
        }

        if (!found) {
            printf("no match found.\n");
        } else {
			printf("match found.\n");
		}

        fclose(file);
    }


    return 0;
}
