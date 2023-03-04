# https://www.acmicpc.net/problem/25206
import sys

total = 0
score_dic = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for _ in range(20):
    name, score, achieve, = sys.stdin.readline().split()
    if achieve == "P":
        pass
    else:
        total += float(score) * float(score_dic[achieve])

print(total/20)