# https://www.acmicpc.net/problem/2609

a,b = list(map(int,input().split()))

def GCD(x,y): # 최소공배수(Greatest Common Divisor)

    while(y):
        x,y = y,x%y
    return x


def LCM(x,y): # 최대공약수(Least Common Multiple)
    result = (x*y)//GCD(x,y)
    return result


print(GCD(a,b))
print(LCM(a,b))