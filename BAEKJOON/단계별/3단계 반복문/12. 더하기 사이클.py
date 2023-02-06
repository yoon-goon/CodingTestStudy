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
