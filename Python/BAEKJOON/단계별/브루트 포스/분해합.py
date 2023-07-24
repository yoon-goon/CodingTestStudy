# https://www.acmicpc.net/problem/2231

N = int(input())

for i in range(1, N + 1):
    num = sum(map(int, str(i)))  # 분해
    fin = i + num
    if fin == N:
        print(i)
        break
    if i == N:
        print(0)
