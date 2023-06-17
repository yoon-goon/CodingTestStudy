shape = input("도형의 종류를 입력하세요: ")


def input_rectangle():
    x1 = int(input("x1좌표"))
    y1 = int(input("y1좌표"))
    x2 = int(input("x2좌표"))
    y2 = int(input("y2좌표"))
    return (x1, y1, x2, y2)


def tup_input_rect():
    t1 = tuple()
    lst = ["x1", "y1", "x2", "y2"]
    for s in lst:
        n = int(input(s + " 입력: "))
        t1 += (n,)
    return t1


print(tup_input_rect())
