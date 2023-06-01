import os


lst = input("경로를 입력하세요")
trylist(lst)

def trylist(lst):
    print(os.listdir(lst))


