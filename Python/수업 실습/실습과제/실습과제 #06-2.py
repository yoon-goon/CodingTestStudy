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
    cnt = 0
    for i in cList:
        if i == ch:
            cnt += 1
    return cnt


def countChars(txt):
    # txt = txt.lower()
    alist = []
    blist = []
    if txt == '':
        return None
    for y in txt:
        if y not in alist:
            alist.append(y)
            blist.append([y, findChar(txt, y)])
    return blist


def printList(cList):
    for i in range(len(countChars(cList))):
        print(countChars(cList)[i])


def main():
    printList(t.lower())


main()
