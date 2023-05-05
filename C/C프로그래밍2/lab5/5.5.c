#include <stdio.h>

static char daytab[2][13] =
{
    {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}, //윤년 비윤년 구분
    {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
};
int day_of_year(int year, int month, int day)
{
    int i, leap;
    leap = year%4 == 0 && year%100 != 0 || year%400 == 0; //윤년 확인
    for (i = 1; i < month; i++) // day변수에 1월부터 일수 합산
    {
        day += daytab[leap][i];
    }
    return day;
}

void month_day(int year, int yearday, int *pmonth, int *pday)
{
        int i, leap;

        leap = year%4 == 0 && year%100 != 0 || year%400 == 0;
        for (i = 1; yearday > daytab[leap][i]; i++) //yearday 가 해당 월 일수보다 크면 
                yearday -= daytab[leap][i]; // yearday에서 빼줌
        *pmonth = i; // 월 = 반복횟수
        *pday = yearday;
}

int main()
{
    int year, month, day, yearday;
    int a;
    // 2022-5-5
    year = 2022;
    month = 5;
    day = 5;
    a = day_of_year(year, month, day);
    printf("%d-%d-%d은 %d째 날입니다.\n", year, month, day, a);
    // 2014-5-5
    year = 2014;
    month = 5;
    day = 5;
    a = day_of_year(year, month, day);
    printf("%d-%d-%d은 %d째 날입니다.\n", year, month, day, a);

    //2022년의 200일째
    year = 2022;
    yearday = 200;
    month_day(year, yearday, &month, &day);
        printf("%d년의 %d째 날은 %d월 %d일입니다.\n",year, yearday, month, day);
    //2000년의 300일째
    year = 2000;
    yearday = 300;
    month_day(year, yearday, &month, &day);
        printf("%d년의 %d째 날은 %d월 %d일입니다.\n",year, yearday, month, day);

}

