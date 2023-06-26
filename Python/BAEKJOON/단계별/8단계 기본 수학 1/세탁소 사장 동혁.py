# https://www.acmicpc.net/problem/2720

times = int(input())
moneylst = []
for _ in range(times):
    moneylst.append(int(input()))

for totalM in moneylst:
    output = []
    while totalM > 5:
        quarter = totalM // 25
        totalM = totalM % 25
        dime = totalM // 10
        totalM = totalM % 10
        nickel = totalM // 5
        totalM = totalM % 5
        output = [quarter, dime, nickel, totalM]
    print(*output)
