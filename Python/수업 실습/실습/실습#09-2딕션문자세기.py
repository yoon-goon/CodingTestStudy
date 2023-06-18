
t = input("영문 문자열 입력: ")

d = {}

for ch in t:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)
for i,j in d.items():
    # if i == " ": #띄어쓰기 안세는용
    #     continue
    print(f"{i} : {j}")



# def findChar(cList, ch):
#     if len(cList) > 0:
#         for lst in cList:
#             if lst[0] == ch:
#                 return lst
#     return None
#
# def countChars(txt):
#     clist = []
#     txt = txt.lower()
#     for ch in txt:
#         lst = findChar(clist, ch)
#         if lst == None:
#             clist.append([ch, 1])
#         else:
#             lst[1] += 1
#     return clist
#
# def printList(cList):
#     for lst in cList:
#         if lst[0] == " ": # 띄워쓰기 스킵용
#             continue
#         print(f"{lst[0]}: {lst[1]}")
#
# #lst = countChars("Loreml")
# #printList(lst)
# def main():
#     lst = countChars(t)
#     printList(lst)
#
# main()