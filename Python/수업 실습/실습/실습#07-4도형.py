# def input_rectangle():
#     x1 = int(input("x1좌표"))
#     y1 = int(input("y1좌표"))
#     x2 = int(input("x2좌표"))
#     y2 = int(input("y2좌표"))
#     return (x1, y1, x2, y2)

# def input_triangle():
#     x1 = int(input("x1좌표"))
#     y1 = int(input("y1좌표"))
#     x2 = int(input("x2좌표"))
#     y2 = int(input("y2좌표"))
#     x3 = int(input("x3좌표"))
#     y3 = int(input("y3좌표"))
#     return (x1, y1, x2, y2, x3, y3)
import math


def tup_input_rect():
    t1 = tuple()
    lst = ["x1", "y1", "x2", "y2"]
    for s in lst:
        n = int(input(s + " 입력: "))
        t1 += (n,)
    return t1


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


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


lst = []
for i in range(5):
    shape = input("도형의 종류를 입력하세요: ")
    if shape == "사각형":
        t = tup_input_rect()
        lst.append(shape)
        lst.append(t)
        print(lst)
        size = (t[2] - t[0]) * (t[1] - t[3])
        print(size)
    elif shape == "삼각형":
        t = tup_input_tri()
        lst.append(shape)
        lst.append(t)
        print(lst)
        size = math.sqrt()
    elif shape == "원":
        t = tup_input_circle()
        lst.append(shape)
        lst.append(t)
        print(lst)
        size = t[2] * t[2] * math.pi
