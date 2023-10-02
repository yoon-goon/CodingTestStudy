# https://www.acmicpc.net/problem/11866

n, k = map(int, input().split())

idx = 0
stack = [i for i in range(1, n + 1)]
ans = []

while stack:
    idx += k - 1  # k-1번째 인덱스까지 건너뛰기
    if idx >= len(stack):  # 인덱스가 범위를 넘어갈 경우
        idx %= len(stack)
    ans.append(str(stack.pop(idx)))

print("<", ", ".join(ans), ">", sep="")
