def findChar(cList, ch):
    if len(cList) > 0:
        for lst in cList:
            if lst[0] == ch:
                return lst
    return None


def countChars(txt):
    txt = txt.lower()
    for ch in txt:
        lst = findChar(clist, ch)
        if lst == None:
            clist.append([ch, 1])
        else:
            lst[1] += 1
    return clist


def printList(cList):
    for lst in cList:
        print(f"{lst[0]}: {lst[1]}")


def main():
    f = open("lorem.txt")
    s = f.readline().rstrip("\n")

    global clist
    clist = []

    while s:
        print(s, end="")
        countChars(s)
        s = f.readline().rstrip("\n")
    f.close()

    print("")
    printList(countChars(s))




main()
