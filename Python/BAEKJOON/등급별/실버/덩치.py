# https://www.acmicpc.net/problem/7568
import sys

N = int(input())
e_list = []

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    e_list.append([A, B])

for y in e_list:  # 리스트를 한번 쭉 흝고감
    rank = 1
    for j in e_list:  # 그 이후 요소들을 비교에 사용하기 위해 j 사용
        if y[0] < j[0] and y[1] < j[1]:  # 무게 , 키 둘다 작으면 랭크가 뒤로 밀려나기때문에
            rank += 1
    print(rank, end=" ")
