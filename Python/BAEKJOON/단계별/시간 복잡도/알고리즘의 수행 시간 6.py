# https://www.acmicpc.net/problem/24267

n = int(input())
count = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            count += 1

print(count, "\n3")
