# https://www.acmicpc.net/problem/2720

times = int(input())


for - in range(times):
    output = []
    totalM = int(input())
    while totalM > 5:
        quarter = totalM // 25
        totalM = totalM % 25
        dime = totalM // 25
        totalM = totalM % 10
        nickel = totalM // 5
        totalM = totalM % 5
        
