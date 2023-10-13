# https://www.acmicpc.net/problem/2609

a,b = list(map(int,input().split()))

def GCD(x,y):

    while(y):
        x,y = y,x%y
    return x


print(GCD(a,b))
