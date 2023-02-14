# https://www.acmicpc.net/problem/10809

S = str(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

for i in (alphabet):
    if i in S:
        print(S.index(i), end=" ")
    else:
        print("-1", end=" ")

# find 함수를 사용해서 해결도 가능

S2 = str(input())
alist = 'abcdefghijklmnopqrstuvwxyz'
for i in alist:
    idx = S2.find(i)
    print(idx, end=' ')
