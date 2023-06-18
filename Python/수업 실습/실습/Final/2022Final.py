def readData(filename):
    dic = {}
    typemoney = []

    # with open(filename, encoding='utf-8') as f: #find로 찾기
    #     line = f.readlines()
    #     for i in line:
    #         print(i)
    #         first = i.find(',')
    #         print(first)
    #         a = i[:first].strip()
    #         second = i[first + 1:].find(',')
    #         print(second)
    #         b = i[first:]
    #         print(b)
    #         dic.update({a: b})
    #         print(dic)

    try:
        with open(filename, encoding='utf-8') as f:  # 반복문을 이용해 , 찾는방법
            line = f.readlines()
            for i in line:
                tmp = ''
                type = ''
                price = ''
                tmplist = []
                for y in i:
                    if y == ',':
                        for x in i[len(tmp) + 1:]:
                            if x == ',':
                                for z in i[len(tmp) + 1 + len(type) + 1:]:
                                    price += z
                                break
                            else:
                                type += x
                        break
                    else:
                        tmp += y
                try:
                    dic.update({tmp: [type, int(price.strip())]})
                except ValueError:
                    print("가격에 정수가 아닌 문자열이 있습니다.")
                    return 0

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return 0
    return dic


def printItem(dic, itemName):
    found = 0
    # print(itemName)
    for item in dic:
        if itemName in item:
            type, price = dic[item]
            print(f"상품명: {item}, 분류: {type}, 가격: {price}")
            found = 1
    if found != 1:
        print(f"상품 {itemName}이(가) 없습니다.")
    return


def printCategory(dic, category):
    print(f"분류명 {category}에 해당하는 상품들:")
    found = 0
    for item, info in dic.items():
        # print(item,info)
        item_category = info[0]
        if item_category.lower() == category.lower():
            price = info[1]
            print(f"상품명: {item}, 분류: {item_category}, 가격: {price}")
            found = 1
    if found != 1:
        print(f"분류항목 {category}이(가) 없습니다.")
    return


def printPriceInRange(dic, price1, price2):
    found = 0
    try:
        price1, price2 = int(price1), int(price2)
        for item, info in dic.items():
            item_category = info[0]
            price = int(info[1])
            # print(price)
            if price1 <= price <= price2:
                print(f"상품명: {item}, 분류: {item_category}, 가격: {price}")
                found = 1

        if found != 1:
            print(f"분류항목 {price1}~{price2}에 해당하는 상품이이(가) 없습니다.")
    except ValueError:
        print("정수가 아닌 문자열이 입력됬습니다.")


def main(filename):
    d = readData(filename)
    print(d)

    control = input("명령:데이터 형식으로 입력하세요. ").lower()
    loc = control.find(":")
    inp = control[loc + 1:]
    if inp.find("~"):
        middle = inp.find("~")
        p1 = inp[:middle]
        p2 = inp[middle + 1:]

    # print(control[:loc])
    # print(inp)
    if control[:loc] == "item":
        printItem(d, inp)
    elif control[:loc] == "category":
        printCategory(d, inp)
    else:
        printPriceInRange(d, p1, p2)


main("items.txt")
