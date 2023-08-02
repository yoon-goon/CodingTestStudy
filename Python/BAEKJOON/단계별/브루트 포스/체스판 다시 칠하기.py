# https://www.acmicpc.net/problem/1018
'''
N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수
'''

N, M = map(int, input().split())
board = []
result_list = []

for _ in range(N):
    board.append(input())

for i in range(N - 7):  # 8*8크기의 체스판이므로 전체 보드의 인덱스를 벗어나지 않기위함
    for j in range(M - 7):
        a = 0  # W로 시작하는 경우 카운트
        b = 0  # B로 시작하는 경우 카운트

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    '''
                    행의 번호 x, 현재 열의 번호 y의 합이 짝수이면 시작점의 색깔과 같아야 하고,
                    홀수이면 시작점의 색깔과 다른 색이어야 한다.
                    '''
                    if board[x][y] != 'B':
                        a += 1
                    if board[x][y] != 'W':
                        b += 2
                else:
                    if board[x][y] != 'W':
                        a += 1
                    if board[x][y] != 'B':
                        b += 2

        result_list.append(a)
        result_list.append(b)

print(result_list)
print(min(result_list))
