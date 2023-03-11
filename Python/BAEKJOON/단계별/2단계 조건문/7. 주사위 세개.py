# https://www.acmicpc.net/problem/2480

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a != b and a != c and b != c:
    print(max(a, b, c) * 100)
else:
    if a == b:
        print(1000 + a * 100)
    elif a == c:
        print(1000 + a * 100)
    else:
        print(1000 + b * 100)

'''
a == b or a == c    -> print ~~a~~
b == c              -> print ~~b~~
을 통해 
a != b and a != c and b != c: 를 else로 대체, 간략화 할수 있음
'''