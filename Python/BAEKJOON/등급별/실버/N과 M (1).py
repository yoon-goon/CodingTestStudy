# https://www.acmicpc.net/problem/15649

N, M = map(int,input().split())
s = []

print(N, M)

for i in range(1, N + 1):
    s.append(i)
    print(s)
    s.pop()
