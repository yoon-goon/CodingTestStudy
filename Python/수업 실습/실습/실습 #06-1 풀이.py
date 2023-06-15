def maxValueOutOfList(lst):
   return max(lst)

[1, 8, 3, 0, 10, 5, 4, 15]
def maxValueOutOfList(lst):
   m = lst[0]  # 현재 최대값
   for i in range(1, len(lst)):
       if m < lst[i]:
           m = lst[i]
   return m

[1, 8, 3, 0, 10, 5, 4, 15]

l = [1, 8, 3, 0, 10, 5, 4, 15]
print(maxValueOutOfList(l))