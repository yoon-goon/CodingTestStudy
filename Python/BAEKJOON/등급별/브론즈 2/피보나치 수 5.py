#  https://www.acmicpc.net/problem/10870

n = int(input())

A = list(range(n + 2))


A[0] = 0
A[1] = 1
A[2] = 1

if n == 0:
    print(A[0])
if n == 1 or 2:
    print(1)
else:
    for i in range(3, n + 1):
        A[i] = A[i - 1] + A[i - 2]

print(A[n])
