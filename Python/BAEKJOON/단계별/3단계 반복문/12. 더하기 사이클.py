# https://www.acmicpc.net/problem/1110

original = int(input())
_num = original

count = 0
while 1:
    if _num < 10:
        _num = ("0" + str(_num))

    _num = str(_num)
    later = _num[1]
    _num = str(int(_num[0]) + int(_num[1]))
    if int(_num) >= 10:
        _num = _num[1]

    _num = later + str(_num)

    _num = int(_num)
    count += 1
    if _num == original:
        print(count)
        break

'''
string으로 변환해 각 자리수를 구하는것 보다
int 자료형에서 //10, %10 을 이용해 1의 자리수를 구하는게 계산에는 더 빠른도움이 될것
n//10 으로 첫자릿수
n%10  으로 둘째자릿수

'''