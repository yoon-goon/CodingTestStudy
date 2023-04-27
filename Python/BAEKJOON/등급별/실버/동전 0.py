# https://www.acmicpc.net/problem/11047
import sys

kind, csum = map(int, input().split())
coinL = []
count = 0
i = kind
# print(kind, csum)

for _ in range(kind):
    coinL.append(int(sys.stdin.readline().strip()))

# print(coinL)

while csum != 0: # 시간초과 질문참고하기

    # print(i)
    i -= 1
    if csum - int(coinL[i]) >= 0:
        csum = csum - int(coinL[i])
        # print("coin", coinL[i])
        # print("csum", csum)
        count += 1
        i = kind
    if i <= 0:
        i = kind

print(count)

"""
while csum != 0: # 시간초과 걸림
    for i in range(kind - 1, -1, -1):
        # print(i)
        if csum - int(coinL[i]) >= 0:
            csum = csum - int(coinL[i])
            # print("coin",coinL[i])
            # print("csum",csum)
            count += 1
            break
            
print(count)

"""

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
