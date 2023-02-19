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

# 개선된 풀이

inp = input()
alist = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
ans = 0

for i in inp:
    for y in alist:
        if i in y:
            ans += alist.index(y) + 3

print(ans)
