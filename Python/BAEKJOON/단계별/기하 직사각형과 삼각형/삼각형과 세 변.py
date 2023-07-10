# https://www.acmicpc.net/problem/5073
import sys

a, b, c = 1, 1, 1

while a != 0 and b != 0 and c != 0:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0 and c == 0:
        break
    elif a == b and b == a and c == a:
        print("Equilateral")
    elif max(a, b, c) < a + b + c - max(a, b, c):
        aset = set()
        aset.update([a, b, c])
        if len(aset) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")

'''
set를 이용한 풀이

A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

while A:
    if(sum(L:=[A,B,C]))<=max(L)*2:print("Invalid")
    else:print([0,"Equilateral","Isosceles","Scalene"][len(set(L))])
    A, B, C = input().split()
    A, B, C = int(A), int(B), int(C)
    
'''