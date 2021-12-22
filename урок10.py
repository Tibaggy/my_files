def century(x):
    if x % 100 == 0:
        return x // 100
    elif x % 100 > 0:
        return x // 100 + 1
print(century(1900))
print(century(1705))
print(century(89))
    
