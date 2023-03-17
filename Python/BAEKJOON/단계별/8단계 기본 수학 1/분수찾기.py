# https://www.acmicpc.net/problem/1193


x = int(input())

row = 1  # 몇 번째 행에 속하는지
while x > row:
    x -= row
    row += 1

'''
대각     1행의 합은 2
        2행의 합은 3
        3행의 합은 4
        이런식으로 이어짐
        윗 계산을 통해 x가 몇번째 행인지 파악
'''

if row % 2 == 0:  # A/B 형식으로 생각
    A = x
    B = row - x + 1
else:
    A = row - x + 1
    B = x

print(str(A) + "/" + str(B))
