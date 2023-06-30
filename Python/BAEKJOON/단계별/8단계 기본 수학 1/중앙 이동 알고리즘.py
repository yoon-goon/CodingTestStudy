# https://www.acmicpc.net/problem/2903

n = int(input())
'''
점의 갯수는 한변의 점의 갯수의^2
횟수  변의 점갯수 
1       2       
2       3
3       5
4       9


'''

print((2 ** n + 1) ** 2)
