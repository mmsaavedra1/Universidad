def buscarTodas(a, b):
    ret = ''
    for i, elem in enumerate(a):
        if b == elem:
            ret += (str(i) + " ")

    return ret[:-1]