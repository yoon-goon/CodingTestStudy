#include <stdio.h>

void qsort(double v[], int left, int right)//퀵정렬 배열의 원소가 소수임으로 double로 변경
{
        int i;
        int last;
        void swap(double v[], int i, int j);

        if (left >= right)
                return;
        swap(v, left, (left + right)/2);//중앙 원소를 기준으로 분할하는 과정
        last = left;
        for (i = left + 1; i <= right; i++)
                if (v[i] < v[left])
                        swap(v, ++last, i);
        swap(v, left, last);
        qsort(v, left, last - 1);// 분할된 두 배열을 재귀적으로 qsort
        qsort(v, last + 1, right);
}

void swap(double v[], int i, int j)// 두 원소를 교환하는 swap 함수
{
        double temp;
        temp = v[i];
        v[i] = v[j];
        v[j] = temp;

}

#define ELEMENTS 10 //원소의 수(배열의 크기) 정의

int main(void) {
        double array[] = {1.1, 9.9, 2.2, 8.8, 3.3, 7.7, 4.4, 6.6, 5.5, 0.0};
        double len = sizeof(array) / sizeof(double);// len = 배열의 길이
        for (int i = 0; i < 10; i++){
            printf("%.1f ",array[i]); // 정리전 배열
        }
        printf("\n");
        qsort(array, 0, 9);
        for (int i = 0; i < 10; i++){
            printf("%.1f ",array[i]); // 소트 후 배열
        }

        printf("\n");
    return 0;
}
