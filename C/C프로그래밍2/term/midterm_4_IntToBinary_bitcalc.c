#include<stdio.h>
#include<stdlib.h>
int main(){
        int a[10],n,i;

        printf("십진수를 입력하세요: ");
        scanf("%d",&n);//십진수 입력    
        for(i=0;n>0;i++)    //비트연산 과정
        {
                a[i]=n%2;
                n=n/2;
        }
        for(i=i-1;i>=0;i--)
        {
                printf("%d",a[i]);
        }
        if (n == 0)// 0값 처리
                printf("0");
        printf("\n");
        return 0;
}
