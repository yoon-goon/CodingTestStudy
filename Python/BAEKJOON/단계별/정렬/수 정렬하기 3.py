# https://www.acmicpc.net/problem/10989 카운팅 정렬을 사용하는 문제

n = int(input())

lst = [0] * 10001

for _ in range(n):
    a = int(input())
    lst[a] += 1

print(lst)