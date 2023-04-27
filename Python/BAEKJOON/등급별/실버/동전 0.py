# https://www.acmicpc.net/problem/11047
import sys

kind, csum = map(int, input().split())
coinL = []
sum = 0
count = 0
print(kind, csum)

for i in range(kind):
    coinL.append(sys.stdin.readline().strip())

print(coinL)

for i in range(kind - 1, -1, -1):
    if sum == csum:
        break
    sum += int(coinL[i])
    count += 1
    if sum > csum:
        sum -= int(coinL[i])
        count -= 1

    print(sum)
    print(i)

print(count)