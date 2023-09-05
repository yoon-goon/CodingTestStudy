# https://www.acmicpc.net/problem/10816
import sys

''' #시간초과 발생
int(sys.stdin.readline())
own = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))
result = [0] * m

for i in own:
    if i in compare:
        result[compare.index(i)] += 1

print(*result)
'''
# dict 사용해 시간 단축
int(sys.stdin.readline())
own = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

cnt = {}

for i in own:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in compare:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')
