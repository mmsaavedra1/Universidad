def strFloat(a):
    sep = a.find('.')
    r = 0.0
    for i in range(sep):
        r += int(a[i]) * (10**(sep - i - 1))
    for i in range(len(a) - 1 - sep):
        r += int(a[-(i+1)]) * 10 ** -(len(a) - 1 - sep - i)
    return r