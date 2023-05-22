import os

print(os.getcwd())

filename = input("파일이름을 입력하세요: ")


def writeNew(s):
    with open(s, "w") as f1:
        f1.write(lst)


try:
    with open(filename, encoding="utf-8") as f:
        lst = f.readlines()
        newfile = "cr_" + filename
        writeNew(newfile)

except FileNotFoundError:
    filename = input("파일을 찾지 못했습니다. 다시한번 입력해 주세요")
