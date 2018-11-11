def swap(string):
    if len(string) == 2:
        return string[1] + string[0]

    return string[1] + string[0] + swap(string[2:])

entrada = input()
print(swap(entrada))
