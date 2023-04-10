s = input("주민번호입력: ")

if len(s) == 14 and s[6] == '-':
    year = int(s[:2])
    y24 = year >= 24 and (s[7] == '1' or s[7] == '2')
    y23 = year <= 23 and (s[7] == '3' or s[7] == '4')
    


else:
    print("부적절한 번호")
