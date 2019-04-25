lst = ["123", "234", "dfgkgd", "err", "3345"]
lst.sort()
print(lst)
lst[1:] = ["sdkff", "ekeokeo", "34u390ru"]
print(lst)
try:
    lst.remove(0)
except ValueError or ArithmeticError as e:
    print(e)
print(lst)
print("{1:4f}sdf".format("sdkf", 2324.23424))


import random
import datetime
random.seed(datetime.datetime.now().second)

a=random.randint(1, 7)
print(a)

import turtle

t=turtle.Turtle()

import os
os.system("pause")

