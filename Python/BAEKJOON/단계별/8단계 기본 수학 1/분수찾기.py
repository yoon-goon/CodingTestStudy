# https://www.acmicpc.net/problem/1193


x = int(input())

row = 1  # 몇 번째 행에 속하는지
while x > row:
    x -= row
    row += 1

if row % 2 == 0:  # A/B 형식으로 생각
    A = x
    B = row - x + 1
else:
    A = row - x + 1
    B = x

print(str(A) + "/" + str(B))
