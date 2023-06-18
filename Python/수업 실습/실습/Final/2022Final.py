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
    pass



def main(filename):
    print(readData(filename))

main("items.txt")