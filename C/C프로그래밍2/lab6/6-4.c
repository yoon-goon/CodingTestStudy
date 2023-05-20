#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#define MAXWORD 100
#define BUFSIZE 100

struct tnode {
        char *word;
        int count;
        struct tnode *left;
        struct tnode *right;
};

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

        root = NULL; // 초기에 루트 노드를 NULL로 설정
        while(getword(word, MAXWORD) != EOF)
                if(isalpha(word[0]))
                        root = addtree(root, word); // 이진 트리에 단어 추가
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
	int cond;

	if(p == NULL) {  // 새로운 단어가 도착한 경우                     
		p = talloc(); // 새 노드를 만듦
		p->word = strdup(w); // w 는 getword에서 나온 문자열
		p->count = 1;
		p->left = p->right = NULL;
 } 	else if((cond = strcmp(w, p->word)) == 0)
		p->count++;  // 중복된 단어
	else if(cond < 0)// 작은건 왼쪽 서브트리
		p->left = addtree(p->left, w);
	else// 큰건 오른쪽 서브트리
		p->right = addtree(p->right, w);

	return p;
}

struct tnode *talloc(void) {
	return(struct tnode *)malloc(sizeof(struct tnode));
}


void treeprint(struct tnode *p) {
	if(p != NULL) {
	treeprint(p->left); // 왼쪽 서브트리를 순회하여 출력
	printf("%4d %s\n", p->count, p->word);
	treeprint(p->right); // 오른쪽 서브트리를 순회하여 출력
	} 
}

// 이전 함수 재사용

int getch(void)
{
        return (bufp > 0) ? buf[--bufp] : getchar();
        // 0보다 크면 버퍼에 저장되어 있는 것, 저장된 문자 반환. 그렇지 않다면 getchar()로 새로운 문자를 입력, 반환
}

void ungetch(int c)
{
  if (c == EOF)
    return;
  if (bufp >= BUFSIZE)
    printf ("ungetch: too many characters\n");
  else
    buf[bufp++] = c;
}
