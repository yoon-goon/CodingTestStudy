# https://www.acmicpc.net/problem/10809

S = str(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

for i in (alphabet):
    if i in S:
        print(S.index(i), end=" ")
    else:
        print("-1", end=" ")
