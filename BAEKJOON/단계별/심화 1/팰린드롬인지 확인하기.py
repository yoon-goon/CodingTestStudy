# https://www.acmicpc.net/problem/10988

word = input()

if word == reversed(word):
    print(reversed(word))
    print(1)
else:
    print(0)