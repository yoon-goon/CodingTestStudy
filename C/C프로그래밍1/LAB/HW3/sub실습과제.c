#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int c1=1,c2=2,c3=3;
    srand(time(NULL));
    for(int i = 0;i < 5;i++){
        do {
            c1 = rand()%10;
            c2 = rand()%10;
            c3 = rand()%10;
        }   while (c1 == c2 || c2 == c3 || c1== c3);

        printf("%d %d %d\n",c1,c2,c3);


    }



    return 0;
}