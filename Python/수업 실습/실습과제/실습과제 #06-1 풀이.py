def createDivisors(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst


# print(createDivisors(2))
# print(createDivisors(12))
# print(createDivisors(16))

def createDivisorsList(n1, n2):
    # lst = [None, None]
    lst = []
    for i in range(n1):
        lst.append(None)
    for i in range(n1, n2 + 1):
        subList = createDivisors(i)
        lst.append(subList)
    return lst


# print(createDivisorsList(5, 10))

# def printList(lst):
#    print(lst)

# def printList(lst):
#    for subList in lst:
#        print(subList)

# def printList(lst):
#    for i in range(len(lst)):
#        print(lst[i])

# 1, 2, 7, 14, 49, 98
# def printList(lst):
#    for i in range(len(lst)):
#        if lst[i] != None:
#            for j in range(len(lst[i]) - 1):
#                print(str(lst[i][j]) + ", ", end='')
#            print(lst[i][len(lst[i]) - 1])

def printList(lst):
    for i in range(len(lst)):
        subList = lst[i]
        if subList != None:
            for j in range(len(subList) - 1):
                print(str(subList[j]) + ", ", end='')
            print(subList[len(subList) - 1])


def main():
    lst = createDivisorsList(2, 100)
    printList(lst)


if __name__ == "__main__":
    main()

