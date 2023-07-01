# https://www.acmicpc.net/problem/1085
    import sys

    x, y, w, h = map(int, sys.stdin.readline().split())
    horizon = w - x
    vertical = h - y

    print(min(x, y, vertical, horizon))
