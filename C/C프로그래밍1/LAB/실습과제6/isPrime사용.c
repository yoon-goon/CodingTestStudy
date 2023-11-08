#include <stdio.h>
int isPrime(int n){
    int num = 0;
    for (int i=2;i<n;i++){
        if(n%i==0)
            return 0;
    }
    return n;
}

int main() {
    int a;
    printf("1부터 입력한 숫자까지의 모든 소수를 찾습니다: ");
    scanf("%d",&a);
    for(int y=2;y<=a;y++){
        int temp = isPrime(y);
        if (temp != 0)
            printf("%d ",temp);

    }

    return 0;
}