# https://www.acmicpc.net/problem/5622


inp = input()
alist = ["", "", "A", "D", "G", "J", "M", "P", "T", "W"]
blist = ["", "", "B", "E", "H", "K", "N", "Q", "U", "X"]
clist = ["", "", "C", "F", "I", "L", "O", "R", "V", "Y"]
dlist = ["", "", "", "", "", "", "", "S", "", "Z"]
ans = 0

for i in inp:
    ans += 1
    if i in alist:
        ans += alist.index(i)
    elif i in blist:
        ans += blist.index(i)
    elif i in clist:
        ans += clist.index(i)
    else:
        ans += dlist.index(i)

print(ans)
