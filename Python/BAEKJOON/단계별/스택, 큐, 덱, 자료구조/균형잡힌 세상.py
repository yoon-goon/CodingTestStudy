# https://www.acmicpc.net/problem/4949
import sys

input = sys.stdin.readline

while True:
    T = input()
    lst = []

    if T[0] == '.':
        break

    for i in T:
        if i == '[' or i == '(':
            lst.append(i)
        elif i == ']':
            if len(lst) > 0 and lst[-1] == '[':
                lst.pop()
            else:
                lst.append('INVALID')
                break
        elif i == ')':
            if len(lst) > 0 and lst[-1] == '(':
                lst.pop()
            else:
                lst.append('INVALID')
                break

    if len(lst) == False:
        print('yes')
    else:
        print('no')
