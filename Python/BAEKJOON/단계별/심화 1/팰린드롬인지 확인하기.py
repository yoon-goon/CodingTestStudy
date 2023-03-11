# https://www.acmicpc.net/problem/10988

word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)
