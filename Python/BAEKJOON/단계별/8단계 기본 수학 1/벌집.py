# https://www.acmicpc.net/problem/2292

# 1,7,19,37,... (6씩증가)
N = int(input())
cnt = 0
if N == 1:
    print(0)

else:
    while N - 1 > 6 * cnt:
        N = N - (6 * cnt)
        cnt += 1

    print(cnt+1)
