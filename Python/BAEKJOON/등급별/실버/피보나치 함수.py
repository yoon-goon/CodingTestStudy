# https://www.acmicpc.net/problem/1003
import sys


# def fibo(x,a,b): # 재귀는 시간초과
#     if x == 0:
#         a += 1
#         return 0
#     elif x == 1:
#         print(1)
#         return 1
#     else:
#         return fibo(x-1) + fibo(x-2)

'''
0의 개수는 1, 0, 1, 1, 2, 3, 5..
1의 개수는 0, 1, 1, 2, 3, 5, 8..
규칙으로 증가(피보나치 함수와 동일)

'''


t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    zero = [1,0]
    one = [0,1]

