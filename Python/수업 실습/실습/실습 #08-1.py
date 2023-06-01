import os

def trylist(lst):
    try:
        print(os.listdir(lst))
    except FileNotFoundError:
        print("올바르지 않은 경로입니다.")

lst = input("경로를 입력하세요")
trylist(lst)



