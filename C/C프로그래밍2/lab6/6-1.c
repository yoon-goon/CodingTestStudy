#include <stdio.h>
#include <math.h>

int main(void)
{
        struct point {
                int x;
                int y;
        };
        struct point pt1 = {10,20};
        struct point pt2 = {30,40};

        //거리 구하기
        int xds = pt2.x - pt1.x;
        int yds = pt2.y - pt1.y;
        double distance = sqrt(xds * xds + yds * yds);//공식사용
        printf("pt1, pt2 사이 거리: %f\n", distance);

        //면적 구하기
        int w = pt2.x - pt1.x;//가로
        int h = pt2.y - pt1.y;//세로
        int area = w * h;
        printf("pt1, pt2로 만든 사각형 넓이: %d\n", area);

        return 0;

}
