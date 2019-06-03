from scipy.optimize import fsolve
import math

v = 340
t1 = math.sqrt(10016)/v
t2 = math.sqrt(10036)/v
t3 = math.sqrt(10136)/v
t4 = math.sqrt(10116)/v

(x1, y1, z1) = (0, 10, 0)
(x2, y2, z2) = (10, 10, 0)
(x3, y3, z3) = (10, 0, 0)
(x4, y4, z4) = (0, 0, 0)

b = v * (t2 - t1)
c = v * (t3 - t1)
d = v * (t4 - t1)
print(b, c, d)


def func(i):
    x, y, z, a = i[0], i[1], i[2], i[3]
    return [
        (x1 - x) ** 2 + (y1 - y) ** 2 + (z1 - z) ** 2 - a ** 2,
        (x2 - x) ** 2 + (y2 - y) ** 2 + (z2 - z) ** 2 - (a + b) ** 2,
        (x3 - x) ** 2 + (y3 - y) ** 2 + (z3 - z) ** 2 - (a + c) ** 2,
        (x4 - x) ** 2 + (y4 - y) ** 2 + (z4 - z) ** 2 - (a + d) ** 2,
    ]


ans = fsolve(func, [0, 0, 0, 0])
print('position', ans[:3], '\ta長度:', ans[3])
