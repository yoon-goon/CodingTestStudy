# https://www.acmicpc.net/problem/1436

'''
n = int(input())
list = []

# print(str(n - 1) + '666')

for i in range(10000000):
    if '666' in str(i):
        list.append(i)

print(list[n-1])
# 시간이 매우 오래걸림
'''

n = int(input())
i = 666
cnt = 0

while 1:
    if '666' in str(i): # '666'이 들어간 경우에만 걸리므로 667,668 다 건너뛰고 1666까지 가게됨
        cnt += 1
    if cnt == n:
        print(i)
        break
    i += 1
