'''
 실습과제 #04-2의 코드 (재귀호출을 사용하지 않는
코드)를 이용할 것
 find(s, ss, pos)를 구현
 s 문자열의 pos 인덱스부터 시작해서 ss를 찾은 후, 처음
나타나는 인덱스 반환
 반복되는 코드를 반복문을 이용해서 줄일 것
'''

t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."


def find(s, ss, pos):
    # a = s.find(ss, pos)
    for i in len(s[pos:]):
        if s[i] == ss:
            return i


def getNextPeriodPos(txt, startpos):
    if startpos >= len(txt):
        return -1  # find 에서도 자체적으로 -1을 출력하지만 이렇게 구현할 수도 있음
    return txt.find('.', startpos, len(txt))


def getNextLine(txt, startpos):
    if startpos >= len(txt):
        return None
    idx = getNextPeriodPos(txt, startpos)
    if idx == -1:  # . 이 없어도 나머지 문자열을 출력하기위함
        return txt[startpos:]
    else:
        return txt[startpos:idx + 1]


def main():
    idx = 0
    for i in range(8):  # (while not -1)
        print(find(t, '.', idx))
        idx = find(t, '.', idx) + 1
    idx = 0
    for i in range(8):  # (while not None)
        s = getNextLine(t, idx)
        print(s)
        idx = find(t, '.', idx) + 1


main()
