pnum = input()

length = len(pnum)
if length != 14:
    pass

middle = pnum.find('-')

if middle != 6:
    pass

year = int(pnum[:2])
month = int(pnum[2:4])

if month < 1 or month > 12:
    pass

day = int(pnum[4:6])

if year >= 23:
    year = 2000

print(pnum)
print(length)
print(middle)
print(year)
print(month)
