import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# 원의 중심 좌표와 반지름 정의
center = (50, 50)
radius = 30

center2 = (70,50)
rad2 = 10

# 원을 그립니다.
fig, ax = plt.subplots()
circle1 = Circle(center, radius, fill=False)
circle2 = Circle(center2, rad2, fill=False)
ax.add_patch(circle1)
ax.add_patch(circle2)

# 그래프 표시
plt.xlim(50, 80)
plt.ylim(0, 80)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()