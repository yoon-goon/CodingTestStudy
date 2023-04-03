pnum = input()

length = len(pnum)


middle = pnum.find('-')



year = int(pnum[:2])
month = int(pnum[2:4])

if length != 14:
    print("글자수가 부적합합니다.")
elif middle != 6: #
    print("-의 위치가 부적합합니다.")
elif month < 1 or month > 12:
    print("월 입력이 부적합합니다.")

day = int(pnum[4:6])




if year >= 23:
    year = 20 

print(pnum)
print(length)
print(middle)
print(year)
print(month)
