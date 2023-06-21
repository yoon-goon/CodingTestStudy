# https://www.acmicpc.net/problem/2745
'''
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다.
이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
'''

N, a = input().split() # N 진법

print(int(N, int(a)))
