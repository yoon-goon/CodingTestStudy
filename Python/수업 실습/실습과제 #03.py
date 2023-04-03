pnum = input()

length = len(pnum)
middle = pnum.find('-')

year = int(pnum[:2])
month = int(pnum[2:4])
day = int(pnum[4:6])



if year >= 23:
    year = 2000

print(pnum)
print(length)
print(middle)
print(year)
print(month)
