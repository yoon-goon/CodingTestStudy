def inputRect():
    x1 = int(input("X1입력: "))
    y1 = int(input("Y1입력: "))
    x2 = int(input("X2입력: "))
    y2 = int(input("Y2입력: "))
    return (x1, y1, x2, y2)


def inputRect2():
    t = tuple()
    lst = ["x1", "y1", "x2", "y2"]
    for i in lst:
        n = int(input(i + " 입력: "))
        t += (n,)
    return t


def inputTriangle():
    x1 = int(input("X1입력: "))
    y1 = int(input("Y1입력: "))
    x2 = int(input("X2입력: "))
    y2 = int(input("Y2입력: "))
    x3 = int(input("X3입력: "))
    y3 = int(input("Y3입력: "))
    return (x1, y1, x2, y2, x3, y3)


# print(inputRect())
#print(inputTriangle())
print(inputRect2())
