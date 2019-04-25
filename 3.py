import datetime

a = datetime.datetime.now()
#print(str(a.second) + "  " +str(a.microsecond))
# print(a.time())
print([float(x) if float(x) > 0 else -float(x) for x in input().split()])
