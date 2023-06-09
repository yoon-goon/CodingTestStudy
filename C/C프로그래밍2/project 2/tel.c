// Ncurses를 이용한 구현

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ncurses.h>

#define MAX_Contacts 100

struct Contact {
    char name[30];
    char phone[20];
    char memo[40];
};

int compare(const void *a, const void *b) { // qsort에 사용될 비교 함수
    struct Contact *contactA = (struct Contact *)a;
    struct Contact *contactB = (struct Contact *)b;
    return strcmp(contactA->name, contactB->name); // 반환값에 따라 요소 순서 결정 (name)을 기준으로 정렬
}

int main(int argc, char *argv[]) {
    int press = 0;
    initscr();
    printw("Wellcome!!");
    press = getch();
    printw("%d",&press);
    getch();
    endwin();
    if (argc != 2 && (argc < 3 || argc > 5)) {
        printf("사용법: 번호,이름 혹은 메모를 입력하면 일치하는 contacts를 찾습니다.\n새로운 contacts 추가 : -a 이름 전화번호 메모(옵션)\n제거 : -d 이름 or 번호 or 메모.\n알파벳 순 정렬 : -l\n");
        return 1;
    }

    if (strcmp(argv[1], "-a") == 0) { //add 옵션
        if (argc < 4 || argc > 5) { // 입력 갯수 오류
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
        } // 메모칸이 비어있는 경우 처리

        printf("%s %s %s\n", argv[2], argv[3], argv[4]);

        printf("add? [Y/N]: "); // 추가할지 Y/N 입력 받기
        char answer;
        scanf(" %c", &answer);

        if (answer == 'Y' || answer == 'y') {
            // 문자열로 만든 후
            char entry[MAX_Contacts];
            snprintf(entry, MAX_Contacts, "%s:%s:%s\n", argv[2], argv[3], argv[4]);

            // 파일에 내용 추가
            fputs(entry, file);

            printf("data.txt 파일에 추가되었습니다.\n");
        } else {
            printf("저장하지 않고 프로그램을 종료합니다.\n");
        }

        fclose(file);
    } else if (strcmp(argv[1], "-d") == 0) { // Delete 삭제 옵션
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

        // 임시 파일 열기 (파일 초기화하기 위해 w 모드)
        FILE *tempFile = fopen("temp.txt", "w");
        if (tempFile == NULL) {
            printf("임시 파일을 열 수 없습니다.\n");
            fclose(file);
            return 1;
        }

        char line[93]; // name : number : memo
        int deleted = 0;
        int order = 0;
        int selectedContact = 0;

        // 파일 읽어오기
        while (fgets(line, sizeof(line), file) != NULL) {
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");
            // line 버퍼에 파일에서 읽어옴 sizeof(line)을 통해 파일의 끝에 도달하거나 읽을 줄이 없을 때까지 반복
            // 읽어온 줄을 strtok 함수를 사용하여 콜론(:)으로 분리 첫 번째 이후 호출 시에는 NULL을 전달하여 이전 호출 위치에서부터 분리

            if (strstr(name, argv[2]) == NULL && strstr(phone, argv[2]) == NULL && strstr(memo, argv[2]) == NULL) {
                fprintf(tempFile, "%s:%s:%s", name, phone, memo);
            } else {
                order++; // 선택지 번호
                deleted = 1;
                printf("%d %s %s %s\n", order, name, phone, memo);
            } // 연락처에 대해 검색어와 일치하는 경우 deleted 1, order 증가(삭제 단계에서 선택 번호를 위함)
            // 연락처에 대해 검색어와 일치하지 않는 경우 해당 연락처 정보를 tempFile에 그대로 기록(유지)
        }

        if (deleted) {
            printf("which one?: ");
            scanf("%d", &selectedContact);

            // 파일 내용 읽어오기 (쓰기 모드로 열기)
            fclose(tempFile);
            tempFile = fopen("temp.txt", "w");
            if (tempFile == NULL) {
                printf("임시 파일을 열 수 없습니다.\n");
                fclose(file);
                return 1;
            }

            // 파일 읽어오기
            rewind(file); // 포인터를 파일의 처음으로
            order = 0; // 선택지 번호
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

                // 임시 파일 대체
                if (rename("temp.txt", "data.txt") != 0) {
                    printf("임시 파일을 원본 파일로 변경하는 중에 오류가 발생했습니다.\n");
                    return 1;
                }

                printf("연락처가 삭제되었습니다.\n"); // 삭제작업 정상완료
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
    else if (strcmp(argv[1], "-l") == 0) { // 알파벳순 정렬 후 list 출력
        char filename[] = "data.txt";
        FILE *file = fopen(filename, "r");

        if (file == NULL) {
            printf("파일을 열 수 없습니다.\n");
            return 1;
        }

        struct Contact contacts[MAX_Contacts]; // 배열 contacts 선언
        int count = 0; // 연락처 갯수

        char line[93]; //name : number : memo
        while (fgets(line, sizeof(line), file) != NULL) {
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");

            strcpy(contacts[count].name, name); //contacts 배열에 복사
            strcpy(contacts[count].phone, phone);
            strcpy(contacts[count].memo, memo);
            count++;
        }

        fclose(file);

        if (count > 0) {
            qsort(contacts, count, sizeof(struct Contact), compare); // qsort이용 정렬

            for (int i = 0; i < count; i++) {
                printf("%d %s %s %s\n", i + 1, contacts[i].name, contacts[i].phone, contacts[i].memo);
            } // 출력
        } else {
            printf("연락처가 없습니다.\n");
        }
    }
     else {
        // search 구현
        char keyword[40]; // name or number or memo 에서 올 수 있는 최대 크기
        strcpy(keyword, argv[1]);

        char filename[] = "data.txt";
        FILE *file = fopen(filename, "r");

        if (file == NULL) {
            printf("파일을 열 수 없습니다.\n");
            return 1;
        }

        char line[93];
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
            } // 하나라도 keyword를 포함하면
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