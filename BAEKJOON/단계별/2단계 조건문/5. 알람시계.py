# https://www.acmicpc.net/problem/2884

hour, _min = map(int, input().split())

if _min - 45 < 0:
    hour -= 1
    _min = 60 + (_min - 45)
