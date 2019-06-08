from scipy.optimize import fsolve
import math

def dist2(a1, a2):

    sum = 0
    for s in range(len(a1)):
        sum += (a1[s]-a2[s])**2 
    return sum

v = 340
m1 = (0,0,0)
m2 = (10,0,0)
m3 = (0,10,0)
m4 = (0,0,10)
t = (10,10,10)
t1 = math.sqrt(dist2(t, m1))/v
t2 = math.sqrt(dist2(t, m2))/v
t3 = math.sqrt(dist2(t, m4))/v
t4 = math.sqrt(dist2(t, m3))/v

(x1, y1, z1) = (0, 0, 0)
(x2, y2, z2) = (10, 0, 0)
(x3, y3, z3) = (0, 0, 10)
(x4, y4, z4) = (0, 10, 0)

b = v * (t1-t2)
c = v * (t1-t3)
d = v * (t1-t4)
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
