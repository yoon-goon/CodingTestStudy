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
    if (argc != 2 && (argc < 3 || argc > 5)) { // 2일땐 search
        printf("사용법: 번호,이름 혹은 메모를 입력하면 일치하는 contacts를 찾습니다.\n새로운 contacts 추가 : -a 이름 전화번호 메모(옵션)\n제거 : -d 이름 or 번호 or 메모.\n");
        return 1;
    }

    if (strcmp(argv[1], "-a") == 0) { //add
        if (argc < 4 || argc > 5) {
            printf("형식이 틀렸습니다. -a 옵션을 사용할 때는 이름, 전화번호, 메모(필수아님)를 입력하세요.\n");
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

    //fclose(file);
	} 
	else if (strcmp(argv[1], "-d") == 0) {
        if (argc != 3) {
            printf("형식이 틀렸습니다. -d 옵션을 사용할 때는 이름or번호or메모를 입력하세요.\n");
            return 1;
        }

        char filename[] = "data.txt";
        char *keyword = argv[2];

        FILE *file = fopen(filename, "r");
        FILE *tempFile = fopen("temp.txt", "w");

        if (file == NULL || tempFile == NULL) {
            printf("파일을 열 수 없습니다.\n");
            return 1;
        }

        char line[90];
        int deleted = 0;
        int order = 0;

        while (fgets(line, sizeof(line), file) != NULL) {
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");

            if (strstr(name, keyword) == NULL && strstr(phone, keyword) == NULL && strstr(memo, keyword) == NULL) {
                order++;
                fprintf(tempFile, "%d:%s:%s:%s", order, name, phone, memo);
            } else {
                deleted = 1;
                printf("%d %s %s %s\n", order, name, phone, memo);
            }
        }

        fclose(file);
        fclose(tempFile);

        if (!deleted) {
            printf("일치하는 연락처가 없습니다.\n");
            remove("temp.txt");
        } else {
            printf("연락처를 삭제할 번호를 입력하세요 (0은 취소): ");
            int choice;
            scanf("%d", &choice);

            if (choice > 0 && choice <= order) {
                file = fopen("temp.txt", "r");
                tempFile = fopen("newdata.txt", "w");

                if (file == NULL || tempFile == NULL) {
                    printf("파일을 열 수 없습니다.\n");
                    return 1;
                }

                int currentContact = 0;
                order = 0;

                while (fgets(line, sizeof(line), file) != NULL) {
                    char *number = strtok(line, ":");
                    char *name = strtok(NULL, ":");
                    char *phone = strtok(NULL, ":");
                    char *memo = strtok(NULL, ":");

                    currentContact++;
                    if (currentContact != choice) {
                        order++;
                        fprintf(tempFile, "%s:%s:%s", name, phone, memo);
                    }
                }

                fclose(file);
                fclose(tempFile);

                if (remove("data.txt") != 0) {
                    printf("연락처를 삭제하는 중에 오류가 발생했습니다.\n");
                    return 1;
                }
                if (rename("newdata.txt", "data.txt") != 0) {
                    printf("임시 파일을 원본 파일로 변경하는 중에 오류가 발생했습니다.\n");
                    return 1;
                }

                printf("연락처가 삭제되었습니다.\n");
            } else {
                printf("연락처 삭제를 취소합니다.\n");
                remove("temp.txt");
            }
        }
    }
	

	else{
		// search 구현
		char keyword[40];
        strcpy(keyword, argv[1]);

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
			

            if (strstr(name, keyword) != NULL || strstr(phone, keyword) != NULL || strstr(memo, keyword) != NULL) {
                printf("%d %s %s %s\n", order, name, phone, memo);
                found = 1;
				order ++;
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
