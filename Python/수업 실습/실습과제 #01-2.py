import math

h = 15
r = 5
a = math.sqrt(h ** 2 + r ** 2)
SurfaceAreaOfCone = math.pi * r * (a + r)
print("콘의 전체 표면적은: %f" % SurfaceAreaOfCone)