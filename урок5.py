def small(x):
    a = x[1]
    for i in x:
        if i < a:
            a = i
    return a
print(small([34, 15, 88, 2, 3]))

        
