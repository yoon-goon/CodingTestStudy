'''
******-******* 형태로

전체 글자 수('-' 포함) 및 '-'의 위치 확인
 년도와 월, 일 확인(년도는 0~22년은 2000년대, 23~99까
지는 1900년대로 가정)
 월과 일이 적합한지 확인(2월은 윤년이면 29일까지 아니면
28일까지. 그 밖의 달은 30일인지 31일 이내인지 확인)
 '-' 다음 숫자는 2000년 이후 출생자(2000년 포함)는 3, 4번
으로 시작. 그 이전 출생자는 1, 2번으로 시작하는지 확인
'''

num = str(input("주민번호를 입력하세요"))
result = 0

if len(num) != 14:
    print("주민번호의 길이가 잘못됬습니다.")
elif num[6] != '-':
    print("-의 위치가 잘못됬습니다.")

else:
    if 0 <= int(num[:2]) <= 23:
        year = "20" + num[:2]
        print(year)
        if num[7] == '3' or num[7] == '4':
            result = 1
    else:
        year = "19" + num[:2]
        print(year)
        print(num[7])
        if num[7] == '1' or num[7] == '2':
            result = 1
    year = int(year)
    month = int(num[2:4])
    day = int(num[4:6])

    isLeapYear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    m29 = isLeapYear and month == 2 and day <= 29
    m28 = (isLeapYear == False) and month == 2 and day <= 28
    m31 = (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 31
    m30 = (month == 4 or month == 6 or month == 9 or month == 11) and day <= 30


    print(result)
    if m29 or m28 or m31 or m30:
        if result == 1:
            print("적합")
        else:
            print("부적합한 - 다음 첫자리")
    else:
        print("월-일 부적절")

