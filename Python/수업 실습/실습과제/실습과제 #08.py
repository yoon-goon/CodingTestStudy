import os

print(os.getcwd())

filename = input("파일 이름을 입력해주세요: ")


def writeNew(s):
    with open(s, "w") as f1:
        idx = 0
        while idx < len(lst):
            if "#" in lst[idx]:
                # print("주석감지")
                location = lst[idx].find("#")
                f1.write(lst[idx][:location] + "\n") # '#'가 있는 인덱스까지 슬라이싱 하는걸로 구현
            else:
                f1.write(lst[idx])
            idx += 1
        print(s, "파일이 생성되었습니다.")


try:
    with open(filename, encoding="utf-8") as f:
        lst = f.readlines()
        # print(lst)
        newfile = "cr_" + filename
        writeNew(newfile)

except FileNotFoundError:
    try:
        filename = input("파일을 찾을 수 없습니다. 다시 입력해주세요: ")
        with open(filename, encoding="utf-8") as f:
            lst = f.readlines()
            # print(lst)
            newfile = "cr_" + filename
            writeNew(newfile)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
