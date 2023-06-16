lst = []

with open("convert.ini") as f:
    lst2 = f.readlines()
    lst.append(lst2[0].strip())

    new_lst = [lst2[1].strip(), lst2[2].strip()]
    lst.append(new_lst)
print(lst)
