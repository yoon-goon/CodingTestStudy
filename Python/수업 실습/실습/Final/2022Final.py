def readData(filename):
    dic = {}
    typemoney = []

    with open(filename,encoding='utf-8') as f:
        line = f.readlines()
        for i in line:
            print(i)
            first = i.find(',')
            print(first)
            a = i[:first].strip()
            b = i[first:].find(',')
            dic.update({a:b})
            print(dic)




    # with open(filename,encoding='utf-8') as f: #반복문을 이용해 , 찾는방법
    #     line = f.readlines()
    #     for i in line:
    #         tmp = ''
    #         tmplist = []
    #         for y in i:
    #             if y == ',':
    #                 for y in
    #                 break
    #             else:
    #                 tmp += y
    #         print(tmp)



    return line


print(readData("items.txt"))


