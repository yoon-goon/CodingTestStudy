#include <stdio.h>
#include <string.h>

int mystrlen(char *s){
	int n;
	for(n=0;*s != '\0'; s++)
		n++;
	return n;
}

int main(void)
{
	char *s[] = {"This is Lab5", "Easy C Programming", "Have fun"};

	printf("with strlen()\n");
	int n = (int)(sizeof(s)/sizeof(char *));
	for (int i = 0; i < n; i++)
		printf("%s %d\n",*(s+i),(int)strlen(s[i]));
	putchar('\n');

	for (int i=0;i<3;i++)
		printf("%s %d\n",*(s+i),(int)mystrlen(s[i]));
	putchar('\n');
}