# https://www.acmicpc.net/problem/2485
import sys

n = int(sys.stdin.readline())
lst = []
a = int(sys.stdin.readline())
st = set()
final = set()
st.add(a)
for _ in range(n-1):
    b = int(sys.stdin.readline())
    st.add(b)
    lst.append(b-a)
    a = b


print(st)
print(min(lst))

while i <= max(st):
    