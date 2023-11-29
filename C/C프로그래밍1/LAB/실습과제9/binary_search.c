#include <stdio.h>
#define SIZE 16

int bSearch(int lst[], int key){
    int low,mid,high;
    low = 0;
    high = SIZE - 1;
    while(low<=high){
        printf("[%d %d]\n",low,high);
        mid=(low+high)/2;
        if(key == lst[mid])
            return mid;
        else if(key>lst[mid])
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;//에러표시
}




int main()
{
    int key;
    int grade[SIZE] = {2,6,11,13,18,20,22,27,29,30,34,38,41,42,45,47};
    printf("탐색할 값을 입력하세요: ");
    scanf("%d",&key);
    printf("탐색결과 = 인덱스%d\n",bSearch(grade,key));


    return 0;
}
