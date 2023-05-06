#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXLINES 5000
#define MAXLEN 1000  


char *lineptr[MAXLINES];

int Mgetline(char s[], int lim)//my getline 이전코드 사용
{
        int c, i;

        for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; i++)
                s[i] = c;
        if (c == '\n') {
                s[i++] = c;
        }
        s[i] = '\0';
        return i;
}

int readlines(char *lineptr[], int maxlines)// 이전코드 사용
{
        int len, nlines;
        char *p, line[MAXLEN];

        nlines = 0;
        while ((len = Mgetline(line, MAXLEN)) > 0)
                if (nlines >= maxlines || (p = malloc(len)) == NULL)
                        return -1;
        else {
                line[len - 1] = '\0';
                strcpy(p, line);
                lineptr[nlines++] = p;
        }
        return nlines;
}

void writelines(char *lineptr[], int nlines)// 이전코드 사용
{
        int i;

        for (i = 0; i < nlines; i++)
                printf("%s\n", lineptr[i]);
}

void Mqsort(void *v[], int left, int right, int (*comp)(void *, void*))// 포인터배열을 정렬
{
        int i, last;
        void swap(void *v[], int, int);

        if (left >= right)
                return;
        swap(v, left, (left + right)/2);
        last = left;
        for (i = left+1; i <= right;i++)
                if ((*comp)(v[i],v[left])<0)
                        swap(v,++last,i);
        swap(v,left,last);
        Mqsort(v,left,last-1,comp);
        Mqsort(v,last+1,right,comp);
}

void swap(void *v[],int i, int j)//교재 코드사용
{
        void *temp;
        temp = v[i];
        v[i] = v[j];
        v[j] = temp;
}

int numcmp(const char *s1, const char *s2)//numcmp 와 strcmp 의 타입이 다르기 때문에 numcmp parameter에 const
{
        double v1,v2;
        v1 = atof(s1);
        v2 = atof(s2);
        if (v1 < v2)
                return -1;
        else if (v1 > v2)
                return 1;
        else
                return 0;
}

int main(int argc, char *argv[])
{
        int nlines;
        int numeric = 0;//-n 입력 처리를 위함

        if (argc > 1 && strcmp(argv[1], "-n") == 0)//-n 입력시
                numeric = 1;
        if ((nlines = readlines(lineptr, MAXLINES)) >= 0) {
                Mqsort((void **) lineptr, 0, nlines-1, (int (*)(void *, void *))(numeric ? numcmp : strcmp));
                // numeric 여부에 따라 numcmp strcmp 둘중 하나 사용
                printf("\nAfter sort.\n");
                writelines(lineptr, nlines);
                return 0;
        }
}
