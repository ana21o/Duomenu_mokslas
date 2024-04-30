def sudetis(a, b):
    return a + b

def atimtis(a, b):
    return a - b

def daugyba(a, b):
    if a is None or b is None:
        raise Exception('nera argumentu!')
    return a * b

def dalyba(a, b):
    return a / b

def ar_lyginis(skaicius):
    return skaicius % 2 == 0

def suapvalinta_dalyba(a, b):
    return round(a/b, 1)

def prideti_i_zodyna(zodis):
    zodynas = {'raktas': zodis}
    return zodynas