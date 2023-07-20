# https://www.acmicpc.net/problem/24313
import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(input())
n0 = int(input())

fn = a1 * n0 + a0
gn = c * n0

if fn <= gn and a1 <= c: # a0가 음수인 경우엔 a1 <= c 도 성립해야함
    print(1)
else:
    print(0)
