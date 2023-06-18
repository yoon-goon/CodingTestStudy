
t = input("영문 문자열 입력: ")


def findChar(cList, ch):
    if len(cList) > 0:
        for lst in cList:
            if lst[0] == ch:
                return lst
    return None

def countChars(txt):
    clist = []
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
        if lst[0] == " ": # 띄워쓰기 스킵용
            continue
        print(f"{lst[0]}: {lst[1]}")

#lst = countChars("Loreml")
#printList(lst)
def main():
    lst = countChars(t)
    printList(lst)

main()