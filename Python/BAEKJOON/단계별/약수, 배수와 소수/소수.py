# https://www.acmicpc.net/problem/2581

allMN = []
M = int(input())
N = int(input())

for i in range(M, N + 1):
    A = []
    if i == 1:
        pass
    else:
        for y in range(1, i + 1):
            if i % y == 0:
                A.append(y)
    if len(A) == 2:
        allMN.append(i)

print(sum(allMN))
print(min(allMN))
