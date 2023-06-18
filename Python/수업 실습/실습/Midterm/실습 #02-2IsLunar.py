
year = int(input("년도를 입력하세요"))

if year % 4 == 0 or year % 400 == 0 :
    if year % 100 == 0 and year % 400 != 0:
        print(f"{year}은 윤년이 아닙니다.")
    else:
        print(f"{year}은 윤년입니다.")
else:
    print(f"{year}은 윤년이 아닙니다.")