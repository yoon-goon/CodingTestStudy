# https://www.acmicpc.net/problem/1018
'''
N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수
'''


N, M = map(int, input())
board = []
result_list = []

for _ in range(N):
    board.append(input())
