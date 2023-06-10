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

int main() {
    initscr();
    cbreak();
    noecho();
    curs_set(0);

    //타이틀 출력
    char message[]="Phonebook management Program";
    int ymax,xmax;
    int cury,curx;
    getmaxyx(stdscr,ymax,xmax);


    start_color();
    init_pair(1,COLOR_GREEN,COLOR_WHITE); // 컬러페어
    //att 설정
    attron(COLOR_PAIR(1));
    attron(A_BOLD);
    mvprintw(ymax/2-2,(xmax-strlen(message))/2,"%s",message);
    attroff(COLOR_PAIR(1));


    mvprintw(ymax-1,0,"Press any key to continue.\n",ymax,xmax);
    refresh();
    getch();

    mvprintw(ymax-12,5,"Select what you want.(Press Enter)\n"); // 선택 안내
    refresh();
    attroff(A_BOLD);
    WINDOW *menuwin = newwin(7,xmax-12,ymax-7,0);
    box(menuwin,0,0);
    refresh();
    wrefresh(menuwin);

    keypad(menuwin,TRUE);

    //선택지
    char *choices[5] = {"Search : by Name or Number or Memo","Add : new contact form is name number memo(optional)","Delete: Find it by Name or Number or Memo.","List : Alphabet order","Exit"};
    int choice;
    int highlight = 0;
    char name[30];
    char phone[20];
    char memo[40];
    char keyword[40];

    //방향표를 이용한 선택 구현
    while (1) {
        for (int i = 0; i < 5; i++) {
                if (i == highlight) {
                    wattron(menuwin,A_REVERSE|A_BLINK); // 선택된 항목을 강조,점멸
                }
                mvwprintw(menuwin, i+1, 1, choices[i]);
                wattroff(menuwin,A_REVERSE|A_BLINK);
            }
            choice = wgetch(menuwin);

            switch (choice) {
                case KEY_UP:
                    highlight--;
                    if (highlight <= -1)
                        highlight = 0;
                    break;
                case KEY_DOWN:
                    highlight++;
                    if (highlight >= 5)
                        highlight = 4;
                    break;
                default:
                    break;
                }
            if (choice == 10)
                break;
    }

    if (highlight == 1) { //        add 기능 구현
        WINDOW *addwin = newwin(10, 50, 2, 2);
        box(addwin, 0, 0);
        refresh();
        curs_set(1);

        // 입력 창 생성
        echo(); //입력위치를 보기위해 다시 활성화
        mvwprintw(addwin, 1, 2, "name: ");
        mvwprintw(addwin, 2, 2, "number: ");
        mvwprintw(addwin, 3, 2, "memo (You can leave empty if you want.):");
        mvwprintw(addwin, 7, 2, "Enter to save and exit.");



        mvwgetnstr(addwin, 1, 8, name, 30);
        mvwgetnstr(addwin, 2, 10, phone, 20);
        mvwgetnstr(addwin, 4, 2, memo, 40);

        char filename[] = "data.txt";
        FILE *file = fopen(filename, "a");

        // 입력 받은 정보 파일에 저장
        fprintf(file, "%s:%s:%s\n", name, phone, memo);


        fclose(file);

        // 성공적 수행 안내문 윈도우
        WINDOW *saddwin = newwin(5, 55, ymax/2-2, xmax/2-27);
        box(saddwin, 0, 0);
        curs_set(0);
        mvwprintw(saddwin,2,3,"Successfully Added! (press any key to continue)");
        wrefresh(saddwin);
        getch();
        noecho();
        endwin();
        refresh();
        }

    else if (highlight == 2) { // Delete 기능 구현
        WINDOW *delewin = newwin(ymax-2, xmax, 2, 0);
        box(delewin, 0, 0);
        mvwprintw(delewin, 2, 2, "Input keyword you want to find to Delete:");
        wrefresh(delewin);
        echo();
        mvwgetnstr(delewin, 3, 2, keyword, 40);
        noecho();

        char filename[] = "data.txt";
        int found = 0;
        int order = 1;
        FILE *file = fopen(filename, "r"); // 파일열기
        char line[93]; // name : number : memo
        struct Contact contacts[MAX_Contacts];
        int numContacts = 0;

        //파일 읽어오기
        while (fgets(line, sizeof(line), file) != NULL) {
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");

            // sizeof(line)을 통해 파일의 끝에 도달하거나 읽을 줄이 없을 때까지 반복
            // 읽어온 줄을 strtok 함수를 사용하여 콜론(:)으로 분리 첫 번째 이후 호출 시에는 NULL을 전달하여 이전 호출 위치에서부터 분리

            if (strstr(name, keyword) != NULL || strstr(phone, keyword) != NULL || strstr(memo, keyword) != NULL) {
                strcpy(contacts[numContacts].name, name);
                strcpy(contacts[numContacts].phone, phone);
                strcpy(contacts[numContacts].memo, memo);
                numContacts++;
                found = 1;
            }
            // 연락처에 대해 검색어와 일치하는 경우 found =  1, numContacts 증가(삭제 단계에서 선택 번호를 위함)
            // 연락처에 대해 검색어와 일치하지 않는 경우 해당 연락처 정보를 tempFile에 그대로 기록(유지)
        }

        fclose(file);

        //삭제할 내용이 있을 경우 선택지 기능구현
        if (found) {
            mvwprintw(delewin, 5, 2, "Matching contacts found. Select a contact and Enter to delete:");
            int highlight = 0;
            int choice;
            keypad(delewin, TRUE);

            // 방향표로 선택구현
            while (1) {
                for (int i = 0; i < numContacts; i++) {
                    if (i == highlight) {
                        wattron(delewin, A_REVERSE|A_BLINK); // 선택된 항목을 강조, 점멸
                    }
                    mvwprintw(delewin, i + 6, 2, "%d %s %s %s", i + 1, contacts[i].name, contacts[i].phone, contacts[i].memo);
                    wattroff(delewin, A_REVERSE|A_BLINK);
                }
                choice = wgetch(delewin);

                switch (choice) {
                    case KEY_UP:
                        highlight--;
                        if (highlight < 0) // 범위를 벗어나지 못하도록
                            highlight = 0;
                        break;
                    case KEY_DOWN:
                        highlight++;
                        if (highlight >= numContacts)
                            highlight = numContacts - 1;
                        break;
                    default:
                        break;
                }
                if (choice == 10)
                    break;
            }
            // 성공적 수행 후 안내문 출력
            WINDOW *sdelwin = newwin(10, 55, ymax/2-2, xmax/2-27);
            box(sdelwin, 0, 0);
            mvwprintw(sdelwin,4,55/2-16,"Successfully Deleted %s %s", contacts[highlight].name, contacts[highlight].phone);
            mvwprintw(sdelwin,6,55/2-10,"Press any key to Exit");
            wrefresh(sdelwin);


            if (highlight >= 0 && highlight < numContacts) { // 삭제할내용이 있었을시

                // 삭제 작업 수행
                FILE *tempFile = fopen("temp.txt", "w");
                if (tempFile == NULL) {
                    mvwprintw(delewin, ymax - 4, 2, "Error deleting contact.");
                    wrefresh(delewin);
                    getch();
                    delwin(delewin);
                    endwin();
                    return 1;
                }

                file = fopen(filename, "r");
                order = 0; // 선택지 번호
                // 기존 파일에서 한 줄씩 읽어와서 검색한 연락처와 일치하지 않는 경우에만 임시 파일에 쓰기
                while (fgets(line, sizeof(line), file) != NULL) {
                    char *name = strtok(line, ":");
                    char *phone = strtok(NULL, ":");
                    char *memo = strtok(NULL, ":");

                    if (strcmp(name, contacts[highlight].name) != 0 || strcmp(phone, contacts[highlight].phone) != 0 || strcmp(memo, contacts[highlight].memo) != 0) {
                        fprintf(tempFile, "%s:%s:%s", name, phone, memo);
                        order++;
                    }
                }

                fclose(file);
                fclose(tempFile);
                remove(filename);
                rename("temp.txt", filename);
            }
            else { // 에러처리
                mvwprintw(delewin, ymax - 4, 2, "Invalid selection. Contact not deleted.");
                wrefresh(delewin);
            }
        }
        else { //에러처리
            mvwprintw(delewin, 5, 2, "No matching contacts found. press any key to Exit");
            wrefresh(delewin);
        }
        getch();
        wrefresh(delewin);
        delwin(delewin);
        noecho();

    }
    else if (highlight == 3) { // List 기능 구현
        WINDOW *listwin = newwin(ymax-2, xmax, 2, 0);
        box(listwin, 0, 0);
        mvwprintw(listwin, 2, 2, "Contacts in alphabetical order:");

        char filename[] = "data.txt"; // 파일 열기
        FILE *file = fopen(filename, "r");
        char line[93];
        struct Contact contacts[MAX_Contacts];
        int numContacts = 0;

        // 파일에서 데이터를 읽어와 구조체 배열에 저장
        while (fgets(line, sizeof(line), file) != NULL) {
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");

            strcpy(contacts[numContacts].name, name);
            strcpy(contacts[numContacts].phone, phone);
            strcpy(contacts[numContacts].memo, memo);
            numContacts++;
        }

        fclose(file);

        // 구조체 배열을 알파벳 순으로 정렬
        qsort(contacts, numContacts, sizeof(struct Contact), compare);

        // 정렬된 결과를 출력
        for (int i = 0; i < numContacts; i++) {
            mvwprintw(listwin, i + 4, 2, "%d %s %s %s", i + 1, contacts[i].name, contacts[i].phone, contacts[i].memo);
        }
        getyx(listwin,cury,curx); // 정렬 포맷을 위함
        mvwprintw(listwin,cury+1,2,"Done, press any key to exit");


        wrefresh(listwin);
        getch();
        delwin(listwin);
        endwin();
    }




        //                          검색기능
    else if (highlight == 0){
        WINDOW *searchwin = newwin(ymax-2, xmax, 2, 0);
        box(searchwin, 0, 0);
        mvwprintw(searchwin,2,2,"Input keyword you want to find:");
        wrefresh(searchwin);
        echo();
        mvwgetnstr(searchwin, 3, 2, keyword, 40);



        char filename[] = "data.txt";
        int found = 0;
        int order = 1;
        FILE *file = fopen(filename, "r");
        char line[93];
        while (fgets(line, sizeof(line), file) != NULL) {
        // 파일에서 데이터를 읽어와서 검색어와 일치하는지 확인
            char *name = strtok(line, ":");
            char *phone = strtok(NULL, ":");
            char *memo = strtok(NULL, ":");
            if (strstr(name, keyword) != NULL || strstr(phone, keyword) != NULL || strstr(memo, keyword) != NULL) {
                getyx(searchwin,cury,curx);
                cury = cury + 1;
                found = 1;
                mvwprintw(searchwin,cury,2, "%d %s %s %s",order,name,phone,memo);
                wrefresh(searchwin);
                order = order + 1;

            }


        }
        if (found != 1) { // 검색어를 만족하는 내용이 없는경우
            mvwprintw(searchwin,9,2, "No matching contacts found.");
            wrefresh(searchwin);
        }
        getyx(searchwin,cury,curx);
        mvwprintw(searchwin,cury+1,2, "Press any key to Exit");
        wrefresh(searchwin);


    fclose(file);
    getch();
    }
    // EXIT 기능
    else if (highlight == 4){
    WINDOW *exwin = newwin(5, 55, ymax/2-2, xmax/2-27);
        box(exwin, 0, 0);
        mvwprintw(exwin,2,2,"Exit without running (press any key to continue)");
        wrefresh(exwin);
        getch();
        endwin();
    }



    endwin();
    return 0;
}