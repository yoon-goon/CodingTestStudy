t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."

'''
 이전 슬라이드에서 보인 텍스트에 있는 글자가 각각
몇 개씩 나타나는지 화면에 출력하는 프로그램을 작
성 (단 모든 글자는 소문자로 변환해서 처리)
 프로그램에서는 전체 텍스트의 내용을 글자와 빈도
수를 리스트로 구성하고, 이들 리스트들을 요소로
하는 리스트를 구성
 리스트의 구성 예
[['l', 19], ['o', 14], ['r', 21], …, ['f', 2]]
'''


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
        print(f"{lst[0]}: {lst[1]}")

#lst = countChars("Loreml")
#printList(lst)
def main():
    lst = countChars(t)
    printList(lst)

main()
