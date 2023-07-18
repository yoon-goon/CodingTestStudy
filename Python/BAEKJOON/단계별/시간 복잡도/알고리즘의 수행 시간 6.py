# https://www.acmicpc.net/problem/24267

n = int(input())
count = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            count += 1

print(count, "\n3")

# 주어진 코드에서 코드1은 "1부터 n까지의 세 수에서 세 수를 뽑는" 경우의 수와 같은 횟수만큼 실행
# -->
print(int((n) * (n - 1) * (n - 2) / 6), "\n3")

'''
n = 7일때
1   2   3 : 5
        4
        5
        6
        7
    3   4 : 4
        5
        6
        7
    4   5 : 3
        6
        7
    5   6 : 2
        7
    6   7 : 1
2   3     : 4
    4     : 5
    5       ...
    6
3   4
    5
    6
4   5
    6
5   6

5+4+3+2+1+4+3+2+1+3+2+1+2+1+1 = 35
'''
