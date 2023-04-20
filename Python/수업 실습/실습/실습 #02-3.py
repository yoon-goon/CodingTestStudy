year = int(input("년"))
month = int(input("월"))
day = int(input("일"))
lunar = 0
tmpdoy = (month - 1) * 31 + day
doy = 0

if year % 4 == 0 or year % 400 == 0:
    if year % 100 == 0 and year % 400 != 0:
        lunar = 0
    else:
        lunar = 1

if month >= 3:
    doy = tmpdoy - ((4 * month + 23) // 10)
    if lunar == 1:
        doy += 1
else:
    doy = tmpdoy


print(doy)
