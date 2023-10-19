# https://www.acmicpc.net/problem/10866

import sys

n = int(input())
deck = []

for _ in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push_front':
        deck.insert(0, a[1])
    elif a[0] == 'push_back':
        deck.append(a[1])
    elif a[0] == 'pop_front':
        if deck:
            print(deck.pop(0))
        else:
            print(-1)
    elif a[0] == 'pop_back':
        if deck:
            print(deck.pop(-1))
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(deck))
    elif a[0] == 'empty':
        if deck:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)
