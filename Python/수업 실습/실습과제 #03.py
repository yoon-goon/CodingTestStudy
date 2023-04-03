print("주민번호를 입력하세요:")
pnum = input()

length = len(pnum)

middle = pnum.find('-')

year = int(pnum[:2])
month = int(pnum[2:4])
day = int(pnum[4:6])

result = 1

if length != 14:
    print("글자수가 부적합합니다.")
    result = 0
if middle != 6:  #
    print("-의 위치가 부적합합니다.")
    result = 0
if month < 1 or month > 12:
    print("월 입력이 부적합합니다.")
    result = 0

if month in [4, 6, 9, 11]:
    if day > 30:
        print("30일까지만 있는 월입니다.")
        result = 0
else:
    if day > 31:
        print("31일이 넘는값을 입력했습니다.")
        result = 0

if year >= 23:  # 수정필요 윤년계산도 추가해야함
    if pnum[7] == 3 or pnum[7] == 4:
        print("2000년 이전 출생자는 1,2로 시작해야합니다.")
        result = 0
else:
    if pnum[7] == 1 or pnum[7] == 2:
        print("2000년 이후 출생자는 3,4로 시작해야합니다.")
        result = 0

print(pnum)
print(length)
print(middle)
print(year)
print(month)

if result == 1:
    print("주민등록번호가 적합합니다.")
else:
    print("주민등록번호가 부적합합니다.")