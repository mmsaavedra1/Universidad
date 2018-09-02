def strReplace(a, b, c):
    d = a.split()
    e = [i for i, j in enumerate(d) if j == b]
    for i in range(len(e)):
        d[e[i]] = c
    return ' '.join(d)
