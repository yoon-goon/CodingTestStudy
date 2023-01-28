# https://blog.naver.com/xhaktm1122/222846963594

a_list = ('a', 'b', 'c', 'd', 'e')
print(a_list)
# ('a', 'b', 'c', 'd', 'e') 패킹


b_list = (1, 2, 3, 4, 5)
a, b, c, d, e = b_list
print(a, b, c, d, e)
# 1 2 3 4 5 언패킹


print(*a_list)
print(*b_list)