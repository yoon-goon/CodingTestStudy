# https://www.acmicpc.net/problem/10866

import sys

n = int(input())

deck = []

for _ in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push_front':
        deck.insert(0,a[1])
    elif a[0] == 'push_back':
        deck.append(a[1])
