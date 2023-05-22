import os

print(os.getcwd())

filename = input("파일이름을 입력하세요: ")  # 주석 1번
try:
    with open(filename, encoding="utf-8") as f:  # 주석 2번
        lst = f.readlines()

except FileNotFoundError:
    filename = input("파일을 찾지 못했습니다. 다시한번 입력해 주세요")  # 주석 3번
