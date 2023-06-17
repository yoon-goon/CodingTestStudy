import math

def inputRect():
   x1 = int(input("X1 입력: "))
   y1 = int(input("y1 입력: "))
   x2 = int(input("X2 입력: "))
   y2 = int(input("y2 입력: "))
   return (x1, y1, x2, y2)

def inputRect2():
    t = tuple()
    lst = ["x1", "y1", "x2", "y2"]

    for s in lst:
        n = int(input(s + " 입력: "))
        t += (n,)
    return t

#t = inputRect2()
#print(t)

def inputTriangle():
   x1 = int(input("X1 입력: "))
   y1 = int(input("y1 입력: "))
   x2 = int(input("X2 입력: "))
   y2 = int(input("y2 입력: "))
   x3 = int(input("X3 입력: "))
   y3 = int(input("y3 입력: "))
   return (x1, y1, x2, y2, x3, y3)

#t = inputTriangle()
#print(t)

def inputShape(lst):
    t = tuple()
#    lst = ["x1", "y1", "x2", "y2"]

    for s in lst:
        n = int(input(s + " 입력: "))
        t += (n,)
    return t

#r = inputShape(["x1", "y1", "x2", "y2"])
#print(r)

#t = inputShape(["x1", "y1", "x2", "y2", "x3", "y3"])
#print(t)

#c = inputShape(["x", "y", "r"])
#print(c)

def createShapeList(n):
    shapeList = list()
    for i in range(n):
        s = input("도형 모양 입력: ")
        if s == "사각형":
            t = inputShape(["x1", "y1", "x2", "y2"])
        elif s == "삼각형":
            t = inputShape(["x1", "y1", "x2", "y2", "x3", "y3"])
        elif s == "원":
            t = inputShape(["x", "y", "r"])
        else:
            print("잘못된 도형 이름이 입력되었습니다.")
            return None
        shapeList.append(s)
        shapeList.append(t)
    return shapeList

def getAreaOfRect(t):
#    x1 = t[0]
#    y1 = t[1]
#    x2 = t[2]
#    y2 = t[3]
#    return (x2 - x1) * (y1 - y2)
    return (t[2] - t[0]) * (t[1] - t[3])

def getAreaOfCircle(t):
    return t[2] * t[2] * math.pi

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def getAreaOfTriangle(t):
    a = distance(t[0], t[1], t[2], t[3])
    b = distance(t[0], t[1], t[4], t[5])
    c = distance(t[2], t[3], t[4], t[5])
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

lst = createShapeList(5)
print(lst)
for i in range(0, len(lst), 2):
    if lst[i] == "사각형":
        area = getAreaOfRect(lst[i + 1])
    elif lst[i] == "삼각형":
        area = getAreaOfTriangle(lst[i + 1])
    elif lst[i] == "원":
        area = getAreaOfCircle(lst[i + 1])
    print(f"모양: {lst[i]}, 넓이: {area}")
