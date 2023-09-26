# https://www.acmicpc.net/problem/13909
'''
import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(1, n + 1): # 브루트포스로 진행하면 초과 발생
    if i ** 2 <= n:
        cnt += 1
print(cnt)
# https://velog.io/@pompom/백준Python-13909-창문-닫기 참고
# 그냥 입력받은 n까지 중에 가장 큰 제곱수의 제곱근을 출력하기만 하면 된다. (24 -> 16 -> 4 출력)
'''

n = int(input())
print(int(n*(1/2)))