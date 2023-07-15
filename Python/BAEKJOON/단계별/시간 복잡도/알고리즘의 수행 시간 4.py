# https://www.acmicpc.net/problem/24265

n = int(input())
count = 0

for i in range(n - 1):
    y = i + 1
    for y in range(n):
        count += 1
print(count, "\n2")
