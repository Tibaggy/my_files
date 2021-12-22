def find(a):
    f = 0
    for i in a:
        f += i
    l = f / len(a)
    return l
print(find([1, 2, 3, 5]))

