print("주민번호를 입력하세요(******-*******):")
pnum = input()

middle = pnum.find('-')

year = int(pnum[:2])
month = int(pnum[2:4])
day = int(pnum[4:6])
Lunar = 0
result = 1

if len(pnum) != 14:
    print("글자수가 부적합합니다.")
    result = 0
if middle != 6:  
    print("-의 위치가 부적합합니다.")
    result = 0
if month < 1 or month > 12:
    print("월 입력이 부적합합니다.")
    result = 0

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # 윤년 계산
    Lunar = 1

if day > 31:
    print("31일이 넘는값을 입력했습니다.")
    result = 0
elif month in [4, 6, 9, 11]:
    if day > 30:
        print("30일까지만 있는 월입니다.")
        result = 0
else:
    if month == 2:
        if Lunar == 1:
            if day > 29:
                print("윤년에는 29일까지입니다.")
                result = 0
        else:
            if day > 28:
                print("윤년이 아닌 2월은 28일까지입니다.")
                result = 0

if int(pnum[middle + 1]) > 4:
    print("- 이후 첫자리는 1~4로 시작해야합니다.")
    result = 0
elif year > 23:  # 수정필요 추가해야함
    if int(pnum[middle + 1]) == 3 or int(pnum[middle + 1]) == 4:
        print("2000년 이전 출생자는 - 이후 1,2로 시작해야합니다.")
        result = 0
else:
    if int(pnum[middle + 1]) == 1 or int(pnum[middle + 1]) == 2:
        print("2000년 이후 출생자는 - 이후 3,4로 시작해야합니다.")
        result = 0

if result == 1:
    print("주민등록번호가 유효합니다.")
else:
    print("주민등록번호가 유효하지 않습니다.")
