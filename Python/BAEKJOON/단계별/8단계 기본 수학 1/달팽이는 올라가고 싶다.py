# https://www.acmicpc.net/problem/2869
''' 시간초과가 걸리는 풀이
A, B, V = map(int, input().split())
day = 0

while V > A:
    V -= A
    if V > 0:
        V += B
    day += 1

print(day + 1)
'''

A, B, V = map(int, input().split())
day = 0

while V > A:
    day += V // A
    V = (V // A) * B + V % A
print(day + 1)
