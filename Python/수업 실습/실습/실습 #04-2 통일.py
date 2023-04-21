'''
 isLeapYear(year)
 윤년이면 True 아니면 False를 반환하는 함수
 년도는 1이상일 것이라고 가정

 getDayOfYear(year, month, day)
 년/월/일을 받아서 1월 1일부터의 통일을 반환하는 함
수 (참고로 1월 1일이 1)
 년도가 0 이하이면 0을 반환
 월(month)가 1-12가 아니면 0을 반환
 일(day)에 대해서는 따로 확인 하지 않음

'''


def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def getDayOfYear(year, month, day):
    if year <= 0:
        return 0
    if 0 > month or month > 12:
        return 0
    dayofyear = (month - 1) * 31 + day
    if month >= 3 and month <= 12:
        # 3월 이후에는 이전 달의 일 수를 보정하는 추가 로직 해당 월 이전의 일 수가 빠진 총 일 수를 구합니다.
        dayofyear -= ((4 * month + 23) // 10)
        if isLeapYear(year):
            dayofyear += 1
    return dayofyear


year = int(input("년도를 입력하세요: "))
month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))

dayOfYear = getDayOfYear(year, month, day)
if dayOfYear == 0:
    print("년도 또는 월 정보가 잘못 입력되었습니다. 년도가 1 이상인지, 월이 1-12사이에 있는지 확인해주세요")
else:
    print("통일: " + str(dayOfYear))