import os

print(os.getcwd())

filename = input("input file name: ")


def writeNew(s):
    with open(s, "w") as f1:
        idx = 0
        while idx < len(lst):
            if "#" in lst[idx]:
                print("주석감지")
                f1.write(lst[idx])
            else:
                f1.write(lst[idx])
            idx += 1



try:
    with open(filename, encoding="utf-8") as f:
        lst = f.readlines()
        print(lst)
        newfile = "cr_" + filename
        writeNew(newfile)

except FileNotFoundError:
    try :
        filename = input("Couldn't find the file, input again: ")
        with open(filename, encoding="utf-8") as f:
            lst = f.readlines()
            print(lst)
            newfile = "cr_" + filename
            writeNew(newfile)
    except FileNotFoundError:
        pass

#MP08data.py