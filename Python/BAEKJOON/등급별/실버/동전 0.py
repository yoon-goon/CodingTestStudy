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
    i -= 1 # 큰값부터 넣어야해서 줄여나가는 방식
    if csum - int(coinL[i]) >= 0:
        count += csum // int(coinL[i]) # 몫만큼 실행가능함으로 카운트에 더함
        # print("coin", coinL[i])
        # print("csum", csum)
        csum = csum % int(coinL[i]) # 나머지만큼 남은 돈

print(count)








'''
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
'''
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
