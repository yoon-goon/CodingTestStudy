# 202115060 윤석진


# 1.
def createIdxFileName(filename):
    idxnum = ''
    for i in range(len(filename)):
        if filename[i] == ".":
            idxnum = i
    newfile = filename[:idxnum] + '.idx'
    print(newfile)
    return (newfile)

    # 나머지 코드 작성


# createIdxFileName("Final3data1.txt")


2.


def createIdxFromFile(filename, enc):
    d = dict()  # 인덱스 딕셔너리 생성
    with open(filename, encoding=enc) as f:
        for _ in range(1000):
            line = f.readline().rstrip("\n")
            # print(line)
            spline = line.split()
            # print(spline)
            for key in spline:
                key = key.strip(";")
                key = key.strip(",")
                key = key.strip(".")
                key = key.strip(":")
                key = key.strip('\"')
                # print(key)
                if not key in d:
                    d.update({key: 1})
                else:
                    d.update({key: d[key] + 1})
        return d

        # 나머지 코드 작성


# print(createIdxFromFile("Final3data1.txt", "UTF-8"))

3.
def printDict(d):
    for i in d:
        print(f"{i}:")
    # 나머지 코드 작성
# printDict(createIdxFromFile("Final3data1.txt", "UTF-8"))

# 4.
def saveIdxToFile(filename, enc, d):
    try:
        with open(filename, "w",encoding=enc) as f:
            for i in d:
                f.write(i)
        # 중간 코드 작성
    except FileNotFoundError:
        print(f"{filename}파일을 열수 없습니다.")
        return False
    except LookupError:
        print(f"{filename}파일의 인코딩 방식이{enc}가 아닙니다.")
        return False
    except:
        print(f"{filename}에 인덱스 저장 중 오류 발생")
        return False

# saveIdxToFile(createIdxFileName("Final3data1.txt"),"UTF-8",d)
#
# # 5.
# filename1 = "Final3data1.txt"
# filename2 = "Final3data2.txt"

# 나머지 코드 작성
