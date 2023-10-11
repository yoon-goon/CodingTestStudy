# https://www.acmicpc.net/problem/2798
N, M = map(int, input().split())
sums = []

# print(N, M)

A = list(map(int, input().split()))

# print(A)

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        for k in range(j + 1, len(A)):
            # print(A[i], A[j], A[k])
            if (A[i] + A[j] + A[k]) <= M:
                sums.append(A[i] + A[j] + A[k])

print(max(sums))
