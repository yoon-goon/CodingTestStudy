# https://www.acmicpc.net/problem/2720

times = int(input())

for _ in range(times):
    output = []
    totalM = int(input())
    while totalM > 5:
        quarter = totalM // 25
        print(quarter)
        totalM = totalM % 25
        print(totalM)
        dime = totalM // 10
        totalM = totalM % 10
        nickel = totalM // 5
        totalM = totalM % 5
        output = [quarter, dime, nickel, totalM]
        print(*output)
