#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_Contacts 100

struct Contact {
    char name[30];
    char phone[20];
    char memo[40];
};

int compare(const void *a, const void *b) {
    struct Contact *contactA = (struct Contact *)a;
    struct Contact *contactB = (struct Contact *)b;
    return strcmp(contactA->name, contactB->name);
}

int main(int argc, char *argv[]) {
    if (argc != 2 && (argc < 3 || argc > 5)) {
        printf("사용법: 번호,이름 혹은 메모를 입력하면 일치하는 contacts를 찾습니다.\n새로운 contacts 추가 : -a 이름 전화번호 메모(옵션)\n제거 : -d 이름 or 번호 or 메모.\n알파벳 순 정렬 : -l\n");
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
        } else {
            printf("저장하지 않고 프로그램을 종료합니다.\n");
        }

        fclose(file);
    } else if (strcmp(argv[1], "-d") == 0) {
        if (argc != 3) {
            printf("형식이 올바르지 않습니다. -d 옵션을 사용할 때는 이름, 번호, 또는 메모를 입력하세요.\n");
            return 1;
        }

        // 파일 열기
        FILE *file = fopen("data.txt", "r");
        if (file == NULL) {
            printf("파일을 열 수 없습니다.\n");
            return 1;
        }

        // 임시 파일 열기 (기존 파일을 초기화하기 위해 "w" 모드로 열기)
        FILE *tempFile = fopen("temp.txt", "w");
        if (tempFile == NULL) {
            printf("임시 파일을 열 수 없습니다.\n");
            fclose(file);
            return 1;
        }

        char line[90];
        int deleted = 0;
        int order = 0;
        int selectedContact = 0;

        // 파일 내용 읽어오기
        while (fgets(line, sizeof(line), file) != NULL) {
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");

            if (strstr(name, argv[2]) == NULL && strstr(phone, argv[2]) == NULL && strstr(memo, argv[2]) == NULL) {
                fprintf(tempFile, "%s:%s:%s", name, phone, memo);
            } else {
                order++; // 선택지 번호
                deleted = 1;
                printf("%d %s %s %s\n", order, name, phone, memo);
            }
        }

        if (deleted) {
            printf("지우려는 연락처의 번호를 선택하세요: ");
            scanf("%d", &selectedContact);

            // 파일 내용 읽어오기 (쓰기 모드로 열기)
            fclose(tempFile);
            tempFile = fopen("temp.txt", "w");
            if (tempFile == NULL) {
                printf("임시 파일을 열 수 없습니다.\n");
                fclose(file);
                return 1;
            }

            // 파일 내용 읽어오기
            rewind(file);
            order = 0;
            deleted = 0;
            while (fgets(line, sizeof(line), file) != NULL) {
                char *name = strtok(line, ":");
                char *phone = strtok(NULL, ":");
                char *memo = strtok(NULL, ":");

                if (strstr(name, argv[2]) == NULL && strstr(phone, argv[2]) == NULL && strstr(memo, argv[2]) == NULL) {
                    fprintf(tempFile, "%s:%s:%s", name, phone, memo);
                } else {
                    order++; // 선택지 번호
                    if (order != selectedContact) {
                        fprintf(tempFile, "%s:%s:%s", name, phone, memo);
                    } else {
                        deleted = 1;
                        printf("다음 연락처가 삭제되었습니다: %s %s %s\n", name, phone, memo);
                    }
                }
            }

            if (deleted) {
                // 기존 파일 삭제
                if (remove("data.txt") != 0) {
                    printf("연락처를 삭제하는 중에 오류가 발생했습니다.\n");
                    return 1;
                }

                // 임시 파일 이름 변경
                if (rename("temp.txt", "data.txt") != 0) {
                    printf("임시 파일을 원본 파일로 변경하는 중에 오류가 발생했습니다.\n");
                    return 1;
                }

                printf("연락처가 삭제되었습니다.\n");
            } else {
                printf("선택한 연락처가 존재하지 않습니다.\n");
                remove("temp.txt");
            }
        } else {
            printf("일치하는 연락처가 없습니다.\n");
            remove("temp.txt");
        }

        // 파일 닫기
        fclose(file);
        fclose(tempFile);
    }
    else if (strcmp(argv[1], "-l") == 0) { // list
        char filename[] = "data.txt";
        FILE *file = fopen(filename, "r");

        if (file == NULL) {
            printf("파일을 열 수 없습니다.\n");
            return 1;
        }

        struct Contact contacts[MAX_Contacts];
        int count = 0;

        char line[MAX_Contacts];
        while (fgets(line, sizeof(line), file) != NULL) {
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");

            strcpy(contacts[count].name, name);
            strcpy(contacts[count].phone, phone);
            strcpy(contacts[count].memo, memo);
            count++;
        }

        fclose(file);

        if (count > 0) {
            qsort(contacts, count, sizeof(struct Contact), compare);

            for (int i = 0; i < count; i++) {
                printf("%d %s %s %s\n", i + 1, contacts[i].name, contacts[i].phone, contacts[i].memo);
            }
        } else {
            printf("연락처가 없습니다.\n");
        }
    }
     else {
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
                order++;
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