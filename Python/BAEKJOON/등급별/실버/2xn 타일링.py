# https://www.acmicpc.net/problem/11726

n = int(input())

'''
n 
1일때    1
2       2
3       3
4       5
5       8


즉 방법의 수는 [n-2] + [n-1]
'''

lst = [0, 1, 2]

if n == 0:
    lst = [0]
elif n == 1:
    lst = [1]
else:
    for i in range(3, n + 1):
        lst.append(lst[i - 2] + lst[i - 1])

print(lst[-1] % 10007)
