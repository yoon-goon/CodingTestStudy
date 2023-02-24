# https://www.acmicpc.net/problem/2444

stars = int(input())

for i in range(1, stars + 1):
    if i == 1:
        print(' ' * (stars - i) + '*')
    else:
        print(' ' * (stars - i) + '*' + '**' * (i - 1))
for x in range(stars - 1, 0, -1):
    print(' ' * (stars - x) + '*' + '**' * (x - 1))
