# https://www.acmicpc.net/problem/1654
import sys

k, n = map(int, sys.stdin.readline().split())

lst = []

for i in range(k):
    lst.append(int(sys.stdin.readline()))

# 이진탐색을 위한 세팅
start = 1
end = max(lst)

while start <= end:
    lines = 0  # 만들어진 줄의 갯수
    mid = (start + end) // 2
    print("mid", mid)
    for y in lst:
        lines += (y // mid)  # 각각줄의 길이를 중간값으로 절단

    if lines >= n:  # 만들어진 줄의 갯수가 필요한 갯수보다 많은 경우
        start = mid + 1  # 중간값을 늘려서 최대길이를 늘림
        print(start)
        print(mid)
    else:  # 만들어진 줄의 갯수가 필요한 갯수보다 적은 경우
        end = mid - 1  # 중간값을 줄여서 길이를 줄임
        print(end)
        print(mid)

print(end)
