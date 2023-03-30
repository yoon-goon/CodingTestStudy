#  https://www.acmicpc.net/problem/10870

n = int(input())

A = list(range(n + 3))

#  A[0] = 0
#  A[1] = 1
#  A[2] = 1
A[:3] = [0, 1, 1]

for i in range(3, n + 1):
    A[i] = A[i - 1] + A[i - 2]

print(A[n])
