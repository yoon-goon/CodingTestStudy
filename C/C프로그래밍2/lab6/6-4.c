#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAXWORD 100

struct tnode {
        char *word;
        int count;
        struct tnode *left;
        struct tnode *right;
}

struct tnode *addtree(struct tnode *, char *);
struct tnode *talloc(void);
void treeprint(struct tnode *);
void ungetch(int);
int getword(char *, int);
int getch(void);

char buf[BUFSIZE];
int bufp = 0;

int main()
{
        struct tnode *root;
        char word[MAXWORD];

        root = NULL;
        while(getword(word, MAXWORD) != EOF)
                if(isalpha(word[0]))
                        root = addtree(root, word);
        treeprint(root);
        return 0;
}
int getword( char *word, int lim)
{
    int c, getch(void);
    void ungetch(int);
    char *w = word;

        while (isspace(c = getch()))
                ;

    if(c != EOF) {
        *w++ = c;
    }
    if(!isalpha(c)) {
        *w = '\0';
        return c;
    }
    for ( ; --lim > 0; w++) {
        if (!isalnum(*w = getch())) { // 단어의 다음 글자가 알파벳 또는 숫자가 아닌 경우
            ungetch(*w); // 문자를 다시 입력 버퍼에 넣음
            break;
        }
    }
    *w = '\0';
    return word[0];

}

struct tnode *addtree(struct tnode *p, char *w) {
