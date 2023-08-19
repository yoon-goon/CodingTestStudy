# https://www.acmicpc.net/problem/1427

num = input()
lst = []

for i in num:
    lst.append(int(i))

print(*sorted(lst, reverse=True), sep='')

'''
짧은 풀이
print(*sorted(sys.stdin.readline(), reverse=True), sep="")
'''