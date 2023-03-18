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

''' 시간이 훨씬 단축되긴 했으나 반복문을 사용하는 것 만으로 시간초과

A, B, V = map(int, input().split())
day = 0

while V > A:
    day += V // A
    V = (V // A) * B + V % A
print(day + 1)
'''

A, B, V = map(int, input().split())

day = (V - B) / (A - B)  # 달팽이가 정상에 도달하기 위해서는 V-B미터를 오르고, A-B미터를 올라가는 것을 하루에 반복
if day == int(day):  # 남은 거리 없이 딱 들어맞는 경우
    day = int(day)
else:
    day = int(day) + 1

print(day)
