filename = input("파일이름을 입력하세요: ")

# try:
#     with open(filename) as f:
#         lst = f.readlines()
#
# except FileNotFoundError:
#     filename = input("파일을 찾지 못했습니다. 다시한번 입력해 주세요")
#

with open(filename) as f:

    lst = f.readlines()