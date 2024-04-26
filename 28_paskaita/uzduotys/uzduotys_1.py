# 1 užduotis
# Parašykite funkciją skaiciu_suma(skaiciai), kuri priima sąrašą skaičių ir grąžina jų sumą.
# Parašykite testą, kuris patikrina, ar funkcija teisingai suskaičiuoja skaičių sumą, panaudojant fixture duomenis su įvairiais skaičių sąrašais.

def skaiciu_suma(skaiciai):
    return sum(skaiciai)

# 2 užduotis
# Parašykite funkciją vidurkis(skaiciai), kuri priima sąrašą skaičių ir grąžina jų vidurkį.
# Parašykite testą, kuris tikrina, ar funkcija teisingai skaičiuoja skaičių sąrašo vidurkį, naudojant fixture duomenis su skirtingais skaičių sąrašais.

def vidurkis(skaiciai):
    for sk in skaiciai:
        if not (isinstance(sk, int) or isinstance(sk, float)):
            return 'klaida'
    return sum(skaiciai)/len(skaiciai)

# 3 užduotis
# Parašykite funkciją zodziu_skaicius(tekstas), kuri priima teksto eilutę ir grąžina jos žodžių skaičių.
# Parašykite testą, kuris patikrina, ar funkcija teisingai skaičiuoja žodžių skaičių teksto eilutėje, naudojant fixture duomenis su skirtingomis teksto eilutėmis.

def zodziu_skaicius(tekstas):
    return len(tekstas.split()) 


# 4 užduotis
# Parašykite funkciją unikalios_reiksmes(sarasas), kuri priima sąrašą ir grąžina jo unikalų elementų sąrašą.
# Parašykite testą, kuris patikrina, ar funkcija teisingai grąžina unikalų elementų sąrašą, naudojant fixture duomenis su įvairiais sąrašais.

def unikalios_reiksmes(sarasas):
    sarasas_unikaliu = []
    for elementas in sarasas:
        if not elementas is sarasas_unikaliu:
            sarasas_unikaliu.append(elementas)
    return sarasas_unikaliu
# return [set(sarasas)]