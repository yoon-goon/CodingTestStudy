# https://www.acmicpc.net/problem/2581

allMN = []
M = int(input())
N = int(input())

for i in range(M, N + 1):
    A = []
    if i == 1:
        pass
    else:
        for y in range(1, int(i ** 0.5) + 1):  # 시간초과를 피하기 위해
            if i % y == 0:
                A.append(y)
    if len(A) == 1:  # int(i ** 0.5) 를 사용했기 때문에 2에서 1로 감소
        allMN.append(i)

    print(allMN)
if allMN == []:
    print(-1)
else:
    print(sum(allMN))
    print(min(allMN))
