# https://www.acmicpc.net/problem/1110

_num = int(input())

while 1:
    if _num < 10:
        _num = ("0"+str(_num))

    _num=str(_num)
    _num = int(int(_num[0])+int(_num[1]))

    print(_num)