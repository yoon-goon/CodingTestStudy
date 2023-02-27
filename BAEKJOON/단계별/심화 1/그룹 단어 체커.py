# https://www.acmicpc.net/problem/1316
import sys

nums = int(input())
cnt = 0
word_list = []

for _ in range(nums):
    words = sys.stdin.readline()
    for i in range(1, len(words)):
        if words[i] != words[i-1]:
                word_list.append(words[i-1])
    if len(set(word_list)) == len(word_list):
        cnt += 1



print(cnt)








'''
for _ in range(nums):
    words = sys.stdin.readline()
    for i in range(0, len(words)):
        if words[i] not in word_list:
            word_list.append(words[i])
        else:
            if words[i] == words[i-1]:
'''

