# https://www.acmicpc.net/problem/4673

alist = set(range(1, 10001))
ans = set()
for i in range(1, 10):
    ans.add(i + i)
for y in range(10, 100):
    yx = str(y)
    ans.add(int(yx) + int(yx[0]) + int(yx[1]))
for x in range(100, 1000):
    xx = str(x)
    ans.add(int(xx) + int(xx[0]) + int(xx[1]) + int(xx[2]))
for z in range(1000, 10000):
    zx = str(z)
    ans.add(int(zx) + int(zx[0]) + int(zx[1]) + int(zx[2]) + int(zx[3]))

for i in (sorted(set(alist) - set(ans))):
    print(i)
