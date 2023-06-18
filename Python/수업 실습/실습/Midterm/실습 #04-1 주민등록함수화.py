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


def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def rtYear(number):
    if number[:2].isdigit() == False:
        print("년도가 위치한 자리의 글자가 숫자가 아니면, 오류메시지")
        return 0
    year = int(number[:2])
    y24 = year >= 24 and (s[7] == '1' or s[7] == '2')
    y23 = year <= 23 and (s[7] == '3' or s[7] == '4')
    if y23 or y24:
        if year >= 24:
            year += 1900
        else:
            year += 2000
    return year


def rtMonth(num):
    if num[2:4].isdigit() == False or (int(num[2:4]) < 1 or int(num[2:4]) > 12):
        print("월이 잘못됨")
        return 0
    return int(num[2:4])


def rtDay(num, yr, mth):
    if yr == 0 or (mth < 1 or mth > 12):
        print("년도가 0이거나 월 정보가 1~12사이가 아니라면 오류 출력 후 0 반환")
        return 0
    else:
        day = int(num[4:6])
        m29 = isLeapYear(yr) and mth == 2 and day <= 29
        m28 = (isLeapYear(yr) == False) and mth == 2 and day <= 28
        m31 = (mth == 1 or mth == 3 or mth == 5 or mth == 7 or mth == 8 or mth == 10 or mth == 12) and day <= 31
        m30 = (mth == 4 or mth == 6 or mth == 9 or mth == 11) and day <= 30
        if num[4:6].isdigit() == False or (m29 == False and m28 == False and m31 == False and m30 == False):
            print("숫자가 아니거나 2자리 숫자가 해당 월의 일 범위 내에 포함되지 않으면 오류 메시지 출력하고 0 반환")
            return 0
        else:
            return int(num[4:6])

def next(num,yr):
    if num[7].isdigit() == False:
        print("-다음이 숫자가아님")
        return 0
    if yr < 2000:
        if num[7] != '1' and num[7] != '2':
            print("1900년대인데 1,2가 아님")
            return 0
    else:
        if num[7] != '3' and num[7] != '4':
            print("2000년대인데 3,4가 아님")
            return 0
    return int(num[7])

def isValid(num):
    if len(num) != 14:
        print("주민등록 번호의 길이가 맞지 않습니다")
        return False
    if num[6] != '-':
        print("'-'가 적절한 위치아님")
        return False
    year = rtYear(num)
    month = rtMonth(num)
    a = rtDay(num,year,month)
    b = next(num,year)
    if a == 0 or b == 0:
        print("주민등록번호가 적합하지않습니다")
    else:
        print("주민번호가 적합합니다.")




s = input("주민번호입력: ")
isValid(s)


'''
if len(s) == 14 and s[6] == '-':
    year = rtYear(s)
    y24 = year >= 24 and (s[7] == '1' or s[7] == '2')
    y23 = year <= 23 and (s[7] == '3' or s[7] == '4')
    if y23 or y24:
        if year >= 24:
            month = int(s[2:4])
            day = int(s[4:6])
            year += 1900
        else:
            month = int(s[2:4])
            day = int(s[4:6])
            year += 2000
        isLeapYear = isLeapYear(year)
        m29 = isLeapYear and month == 2 and day <= 29
        m28 = (isLeapYear == False) and month == 2 and day <= 28
        m31 = (
                          month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 31
        m30 = (month == 4 or month == 6 or month == 9 or month == 11) and day <= 30

        if m29 or m28 or m31 or m30:
            print("적합")
        else:
            print("부적절")
    else:
        print("부적절한 -다음 첫자리")
else:
    print("부적절한 번호")
'''