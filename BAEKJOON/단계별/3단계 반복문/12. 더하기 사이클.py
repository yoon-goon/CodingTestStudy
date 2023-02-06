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
하지만 문제에
먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고,
각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 
앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
라는 조건이 있어 이런식으로 구현
'''