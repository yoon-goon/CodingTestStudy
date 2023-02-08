# https://www.acmicpc.net/problem/5597
import sys

list = []
answer = []
for i in range(28):
    list.append(int(sys.stdin.readline()))

for i in range(30):
    if not i in list:
        
