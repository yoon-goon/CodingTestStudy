#include <stdio.h>

int even(int n){
    if(n%2==1)
        return 1;
    else
        return 0;
}

int main()
{
    int a = 14;
    printf("%d", even(a));

    return 0;
}