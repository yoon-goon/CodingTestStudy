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




while csum != 0:
    for i in range(kind - 1, -1, -1):
        print(i)
        if csum % int(coinL[i]) >= 0 and int(coinL[i]) <= csum :
            csum = csum % int(coinL[i])
            print("coin",coinL[i])
            print("csum",csum)
            count += 1
            break


print(count)
















'''

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

print(count)'''