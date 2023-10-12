# https://www.acmicpc.net/problem/1920

n = int(input())
lst = set(input().split()) # 시간 절약을 위해 set로
m = int(input())
lst2 = list(input().split())

for i in lst2:
    if i in lst:
        print(1)
    else:
        print(0)