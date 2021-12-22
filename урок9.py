# hello
def light(x):
    d = ['green', 'yellow', 'red']
    if x == d[0]:
        return d[1]
    elif x == d[1]:
        return d[2]
    else:
        return d[0]
print(light('green'))
print(light('yellow'))
print(light('red'))
