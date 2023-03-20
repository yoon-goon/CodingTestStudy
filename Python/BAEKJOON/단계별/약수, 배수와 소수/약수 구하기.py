# https://www.acmicpc.net/problem/2501

N, K = map(int, input().split())
A = []

for i in range(1, N + 1):
    if N % i == 0:
        A.append(i)

try:
    print(A[K - 1])
except IndexError:
    print(0)
