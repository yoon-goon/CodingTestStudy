# https://www.acmicpc.net/problem/2908

a, b = input().split()
a, b = a[::-1], b[::-1]

print(max(a, b))

# 간략화

print(max(input()[::-1].split()))
