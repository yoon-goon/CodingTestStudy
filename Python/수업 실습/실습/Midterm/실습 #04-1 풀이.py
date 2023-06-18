num = input("주민등록번호를 ******-*******형태로 입력하세요: ")


def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def getYear(numStr):
    yStr = numStr[:2]
    year = 0
    if yStr.isdigit():
        year = int(yStr)
        if year >= 0 and year <= 21: #문제조건 년도 확인할것
            year = year + 2000
        else:
            year += 1900
    else:
        print("주민등록번호가 잘못 입력되었습니다. 년도가 숫자가 아닙니다.")
    return year


def getMonth(numStr):
    mStr = numStr[2:4]
    month = 0
    if mStr.isdigit():
        month = int(mStr)
        if month >= 0 and month <= 12:
            return month
        else:
            print("주민등록번호가 잘못 입력되었습니다. 월이 범위를 벗어났습니다")
    else:
        print("주민등록번호가 잘못 입력되었습니다. 월이 숫자가 아닙니다")
    return month


def getDay(numStr, year, month):
    if year == 0 or month < 1 or month > 12:
        print("년도 또는 월 정보가 잘못 되었습니다")
        return 0
    dStr = numStr[4:6]
    day = 0
    if dStr.isdigit():
        day = int(dStr)
        if month == 2:
            dayLimit = 28
            if isLeapYear(year):
                dayLimit += 1
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            dayLimit = 31
        else:
            dayLimit = 30
        if day >= 1 and day <= dayLimit:
            return day
        else:
            print("일이", month, "월의 일 범위를 벗어났습니다")


def getSecondNum(numStr, year):
    idx = numStr.index('-')
    nstr = numStr[idx + 1]
    if year < 2000:
        if nstr == '1' or nstr == '2':
            return int(nstr)
        else:
            print("2000년 이전 출생자는 번호가 1 또는 2로 시작해야 합니다")
    elif year >= 2000:
        if nstr == '3' or nstr == '4':
            return int(nstr)
        else:
            print("2000년 1월 1일 이후 출생자는 번호가 3 또는 4로 시작해야 합니다")
    return 0


def isValid(numStr):
    year = getYear(num)
    month = getMonth(num)
    day = getDay(num, year, month)
    n = getSecondNum(num, year)
    if len(num) != 14:
        print("주민등록번호의 길이가 맞지 않습니다")
        return False
    else:
        if (not ('-' in num)) or num[6] != '-':
            print("주민등록번호에 '-'가 없거나 잘못된 위치에 있습니다")
            return False
        else:
            if year > 0 and month > 0 and day > 0 and n >= 1 and n <= 4:
                return True
            else:
                return False


if isValid(num):
    print("주민등록번호가 적합해 보입니다")
else:
    print("주민등록번호가 적합하지 않습니다")
