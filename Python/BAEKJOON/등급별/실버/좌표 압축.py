# https://www.acmicpc.net/problem/18870
import sys

N = int(sys.stdin.readline())

xlist = list(map(int, sys.stdin.readline().split()))

sorted_xlist = sorted(xlist)
count_dict = {}
count = 0

for i in range(N):
    if sorted_xlist[i] not in count_dict:
        count_dict[sorted_xlist[i]] = count
        count += 1

for i in range(N):
    print(count_dict[xlist[i]], end=' ')


















'''

N = int(sys.stdin.readline())

# 자신보다 작은 수 갯수를 출력하면 됨

xlist = list(sys.stdin.readline().split())
xset = sorted(list(set(xlist)))

print(xset)

# print(xlist)

for i in xlist:
    print(xset.index(i),end=' ') # 인덱스를 이용해서 반복문을 한번 더 줄였지만 그래도 시간초과
'''




'''
N = int(input())

# 자신보다 작은 수 갯수를 출력하면 됨

xlist = list(map(int, input().split()))
xset = list(set(xlist))

# print(xlist)

for i in xlist:
    cnt = 0
    for y in range(len(xset)):
        if i > xset[y]:
            cnt += 1
    print(cnt, end=' ')
    
    #시간초과된 풀이
'''

