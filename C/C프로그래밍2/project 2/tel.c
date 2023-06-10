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

int main() {
    initscr();
    cbreak();
    noecho();


    char message[]="Phonebook management Program";
    int ymax,xmax;
    int cury,curx;
    getmaxyx(stdscr,ymax,xmax);


    start_color();
    init_pair(1,COLOR_GREEN,COLOR_WHITE);

    attron(COLOR_PAIR(1));
    attron(A_BOLD);
    mvprintw(ymax/2,(xmax-strlen(message))/2,"%s",message);
    attroff(COLOR_PAIR(1));
    attroff(A_BOLD);

    mvprintw(ymax-1,0,"Press any key to continue.\n",ymax,xmax);
    refresh();
    getch();
    mvprintw(ymax-12,5,"Select what you want.(Press Enter)\n");
    refresh();
    WINDOW *menuwin = newwin(7,xmax-12,ymax-7,0);
    box(menuwin,0,0);
    refresh();
    wrefresh(menuwin);

    keypad(menuwin,TRUE);

    char *choices[5] = {"Search : by Name or Number or Memo","Add : new contact form is name number memo(optional)","Delete: Find it by Name or Number or Memo.","List : Alphabet order","Exit"};
    int choice;
    int highlight = 0;
    char name[30];
    char number[20];
    char memo[40];
    char keyword[40];


    while (1) {
        for (int i = 0; i < 5; i++) {
                if (i == highlight) {
                    wattron(menuwin,A_REVERSE); // 선택된 항목을 강조
                }
                mvwprintw(menuwin, i+1, 1, choices[i]);
                wattroff(menuwin,A_REVERSE);
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
    //printw("Your choice is %s",choices[highlight]);
//    wclear(menuwin);




    if (highlight == 1) { //        add 기능 구현
        WINDOW *addwin = newwin(10, 50, 2, 2);
        box(addwin, 0, 0);
        refresh();

        // 입력 필드 생성
        echo();
        mvwprintw(addwin, 1, 2, "name: ");
        mvwprintw(addwin, 2, 2, "number: ");
        mvwprintw(addwin, 3, 2, "memo (You can leave empty if you want.):");
        mvwprintw(addwin, 7, 2, "Enter to save and exit.");



        mvwgetnstr(addwin, 1, 8, name, 30);
        mvwgetnstr(addwin, 2, 10, number, 20);
        mvwgetnstr(addwin, 4, 2, memo, 40);

        char filename[] = "data.txt";
        FILE *file = fopen(filename, "a");

        // 입력 받은 정보 파일에 저장
        fprintf(file, "%s:%s:%s\n", name, number, memo);


        fclose(file);

        // 종료
        noecho();
        delwin(addwin);
        endwin();
        refresh();
        }

    else if (highlight == 2) { //       Delete 기능 구현
        WINDOW *delewin = newwin(ymax-2, xmax, 2, 0);
        box(delewin, 0, 0);
        mvwprintw(delewin,2,2,"Input keyword you want to find to Delete:");
        wrefresh(delewin);
        echo();
        mvwgetnstr(delewin, 3, 2, keyword, 40);
        char filename[] = "data.txt";
        char tempFilename[] = "temp.txt";
        FILE *file = fopen(filename, "r");
        FILE *tempFile = fopen(tempFilename, "w");
        int found = 0;

        char line[93];
        int contactCount = 0;
        while (fgets(line, sizeof(line), file) != NULL) {
            if (strstr(line, keyword) == NULL) {
                fputs(line, tempFile);
            } else {
                found = 1;
                contactCount++;
                mvprintw(contactCount, 5, "%d. %s", contactCount, line);
            }
        }

        fclose(file);
        fclose(tempFile);

        // 원본 파일을 삭제하고 임시 파일을 원본 파일로 이름 변경
        remove(filename);
        rename(tempFilename, filename);

        if (found) {
            mvprintw(ymax-5, 5, "Contact(s) found. Enter the number to delete: ");
            refresh();

            int selectedContact;
            scanw("%d", &selectedContact);

            if (selectedContact >= 1 && selectedContact <= contactCount) {
                FILE *updatedFile = fopen(filename, "r");
                FILE *updatedTempFile = fopen(tempFilename, "w");
                int currentContact = 0;

                while (fgets(line, sizeof(line), updatedFile) != NULL) {
                    if (strstr(line, keyword) == NULL) {
                        fputs(line, updatedTempFile);
                    } else {
                        currentContact++;
                        if (currentContact != selectedContact) {
                            fputs(line, updatedTempFile);
                        }
                    }
                }

                fclose(updatedFile);
                fclose(updatedTempFile);

                remove(filename);
                rename(tempFilename, filename);

                mvprintw(ymax-3, 5, "Selected contact deleted successfully.");
            } else {
                mvprintw(ymax-3, 5, "Invalid selection. No contact deleted.");
            }
        } else {
            mvprintw(ymax-5, 5, "Contact not found.");
        }

        mvprintw(ymax-1, 5, "Press any key to continue.");
        refresh();
        getch();
        delwin(delewin);
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
            if (strstr(line, keyword) != NULL) {
                getyx(searchwin,cury,curx);
                cury = cury + 1;
                found = 1;
                mvwprintw(searchwin,cury,2, "%d %s %s %s",order,name,phone,memo);
                wrefresh(searchwin);
                order = order + 1;

            }


        }
        if (found != 1) {
            mvwprintw(searchwin,9,2, "There is none of that");
            wrefresh(searchwin);
        }
        getyx(searchwin,cury,curx);
        mvwprintw(searchwin,cury+1,2, "Press any key to Exit");
        wrefresh(searchwin);


    fclose(file);
    }



    getch();
    delwin(menuwin);
    endwin();
    return 0;
}