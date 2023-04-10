s = input("주민번호입력: ")

if len(s) == 14 and s[6] == '-':
    year = int(s[:2])
    y24 = year >= 24 and (s[7] == '1' or s[7] == '2')
    y23 = year <= 23 and (s[7] == '3' or s[7] == '4')
    if y23 or y24:
        if year >= 24:
            year += 1900
        else:
            month = int(s[2:4])
            day = int(s[4:6])
            year += 2000
        isLeapYear = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        m29 = isLeapYear and month == 2 and day <= 29
        m28 = (isLeapYear == False) and month == 2 and day <= 28
        m31 = (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 31
        m30 = (month == 4 or month == 6 or month == 9 or month == 11) and day <= 30

        if m29 or m28 or m31 or m30:
            print("적합")
        else:
            print("부적절")
    else:
        print("부적절한 -다음 첫자리")
else:
    print("부적절한 번호")
