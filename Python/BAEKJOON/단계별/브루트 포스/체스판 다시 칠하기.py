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
        pass

print(board)