import os


def trylist(lst):
    try:
        f = open(lst)
        texts = f.readlines()
        for txt in texts:
            print(txt, end="")
    except FileNotFoundError:
        print("올바르지 않은 이름입니다.\n")
        try:
            lst = input("파일이름을 입력하세요 ")
            f = open(lst)
            texts = f.readlines()
            for txt in texts:
                print(txt, end="")
        except FileNotFoundError:
            print("종료됩니다.")


lst = input("파일이름을 입력하세요 ")

trylist(lst)
