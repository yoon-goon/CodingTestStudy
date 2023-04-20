t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."


def getNextPeriodPos(txt, startPos):
    # print(txt[startPos])
    # print(txt)
    A = txt[startPos:]
    N = A.find(".")
    startPos += N
    if N == -1:
        return -1
    print(startPos)

    return startPos  # getNextPeriodPos(txt, startPos + 1)


def getNextLine(txt, startPos):
    if startPos >= len(txt):
        return None
    A = txt[startPos:]
    N = A.find(".")
    print(txt[startPos:startPos + N + 1].strip())
    # print(startPos)
    startPos += N
    getNextLine(txt, startPos + 1)

    return  # txt[startPos:startPos + N + 1].strip()


def main(txt, startPos):
    idx = getNextPeriodPos(txt, startPos)
    if idx == -1:
        return
    else:
        main(txt, idx + 1)  # 재귀
        if startPos == 0:
            getNextLine(txt, startPos)
    return

    # getNextLine(t, 0)


main(t, 0)
# getNextPeriodPos(t, 0)
# getNextLine(t, 0)


'''
getNextPreiodPos는 main을 재귀해 출력 성공
하지만 getnextline은 main이 리턴해서 역순으로 출력되거나 main을 다시 부르면 getNextPeriodPos 또한 다시 실행되어 완벽하지않은 코드로 작성

'''
