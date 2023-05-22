import os

print(os.getcwd())

filename = input("input file name: ")  # 주석 1번
try:
    with open(filename, encoding="utf-8") as f:  # 주석 2번
        lst = f.readlines()

except FileNotFoundError:
    filename = input("Couldn't find the file, input again")  # 주석 3번
