#include <stdio.h>

int main() {
    int num,cnt = 0,subcnt;
    printf("양의정수를 입력하세요:");
    scanf("%d",&num);


    for(int i=1;i<=num;i++)
    {
        subcnt = 0;
        for(int y=1;y<=i;y++){
            if(i%y==0){
                subcnt++;
            }
        }
        if(subcnt==2){
            printf("%d ",i);
        }
    }
    return 0;
}