def plus(x, y):
    a = x[1]
    for i in x:
        a += i
    for i in y:
        a += i
    return a
print(plus([1, 2, 3], [4, 5, 6]))
