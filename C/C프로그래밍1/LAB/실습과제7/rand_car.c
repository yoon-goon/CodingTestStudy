#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>



void disp_car(int car_num,int distance)
{
    int i ;
    printf("CAR #%d:",car_num);
    for(i=0;i<distance/10;i++){
        printf("*");
    }
    printf("\n");
}