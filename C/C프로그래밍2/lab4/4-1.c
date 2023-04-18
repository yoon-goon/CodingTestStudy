#include <stdio.h>


int max(int i, int j, int k)// max함수 구현
{
        if (i >= j && i >= k) // i가 가장 크거나 같을경우
                return i;
        else if (j >= i && j >= k)// j가 가장 크거나 같을경우
                return j;
        else
                return k;


}

int min(int i, int j, int k)//min함수 구현
{
        if (i <= j && i <= k)//i가 가장 작은경우
                return i;
        else if (j <= i && j <= k)//j가 가장작은경우
                return j;
        else
                return k;


}

int main(void)
{
        int i = 10;
        int j = 20;
        int k = -30;

        printf("Min value is %d\n", min(i,j,k));
        printf("Max value is %d\n", max(i,j,k));

        return 0;
}
