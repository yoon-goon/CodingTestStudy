#  https://www.acmicpc.net/problem/10870

n = int(input())

A = list(range(n))

A[0] = 0
A[1] = 1
A[2] = 1

print(A)

for i in range(3, n):
    A[i] = A[i - 1] + A[i - 2]

print(A[n-1])
