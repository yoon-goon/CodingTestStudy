# https://www.acmicpc.net/problem/2941


inp = input()
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ans = 0

for i in cro_alpha:
    if i in inp:
        ans += inp.count(i)
        inp.replace('l', '',1)

print(ans,inp)
