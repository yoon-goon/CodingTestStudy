# def input_rectangle():
#     x1 = int(input("x1좌표"))
#     y1 = int(input("y1좌표"))
#     x2 = int(input("x2좌표"))
#     y2 = int(input("y2좌표"))
#     return (x1, y1, x2, y2)


def tup_input_rect():
    t1 = tuple()
    lst = ["x1", "y1", "x2", "y2"]
    for s in lst:
        n = int(input(s + " 입력: "))
        t1 += (n,)
    return t1


# def input_triangle():
#     x1 = int(input("x1좌표"))
#     y1 = int(input("y1좌표"))
#     x2 = int(input("x2좌표"))
#     y2 = int(input("y2좌표"))
#     x3 = int(input("x3좌표"))
#     y3 = int(input("y3좌표"))
#     return (x1, y1, x2, y2, x3, y3)

def tup_input_tri():
    t1 = tuple()
    lst = ["x1", "y1", "x2", "y2", "x3", "y3"]
    for s in lst:
        n = int(input(s + " 입력: "))
        t1 += (n,)
    return t1


def tup_input_circle():
    t1 = tuple()
    lst = ["x", "y", "r"]
    for s in lst:
        n = int(input(s + " 입력: "))
        t1 += (n,)
    return t1


for i in range(5):
    shape = input("도형의 종류를 입력하세요: ")
    if shape == "사각형":
        print(tup_input_rect())
    elif shape == "삼각형":
        print(tup_input_tri())
    elif shape == "원":
        print(tup_input_circle())
