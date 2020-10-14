a = 0

def getattr(x):
    global a
    if x == 0:
        return
    a += 1
    return getattr(x-1)


result = getattr(5)
print(a)