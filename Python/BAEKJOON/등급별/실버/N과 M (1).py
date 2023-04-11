# https://www.acmicpc.net/problem/15649

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        s.append(i)
        dfs()
        s.pop()


N, M = map(int, input().split())
s = []

print(N, M)
dfs()
