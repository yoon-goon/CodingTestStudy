# https://www.acmicpc.net/problem/24266

n = int(input())
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1

print(count, "\n3")

print(n * n * n, "\n3")
