# https://www.acmicpc.net/problem/2525

cur_hour, cur_min = map(int, input().split())
time = int(input())

cur_min += time
while cur_min >= 60:
    cur_hour += 1
    cur_min -= 60
if cur_hour >= 24:
    cur_hour -= 24

print(cur_hour, cur_min)
