# https://www.acmicpc.net/problem/11723
import sys

m = int(input())
s = set()

for _ in range(m):
    a = list(sys.stdin.readline().split())

    if len(a) == 2:  # all 명령 시 생성되는 range값들이 정수인 것을 고려, 입력 값을 int로 변환시켜 준다.
        a[1] = int(a[1])  # 안바꾸면 값이 틀리게나옴

    if a[0] == 'add':
        s.add(a[1])
    elif a[0] == 'remove':
        if a[1] in s:
            s.remove(a[1])
    elif a[0] == 'check':
        if a[1] in s:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        if a[1] in s:
            s.remove(a[1])
        else:
            s.add(a[1])
    elif a[0] == 'all':
        s = set(range(1, 21))
    elif a[0] == 'empty':
        s = set()
