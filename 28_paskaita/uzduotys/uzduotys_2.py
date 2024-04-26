# 1 užduotis
# Parašykite funkciją patvirtinti_apmokejima(saskaitos_numeris, suma), kuri kreipiasi į kitą funkciją (patikrinti_likutį(sąskaitos_numeris, suma) šioje funkcijoje galite turėti dictionary, kurio viduje saugosite banko sąskaitų numerius ir jų likučius)
# funkcija patikrinti_likutį tiesiog grąžina True, jeigu sąskaitos likutis yra pakankamas, False jeigu lėšų yra per mažai.
# Funkcija patvirtinti_apmokejima grąžins suformuotą tekstą "Banko sąskaita xxxx-xxxx-xxxx gali/negali atlikti mokėjimą", šis pranešimas bus formuojamas priklausomai nuo patvirtinti_apmokėjimą atsakymo
# Parašykite testų, kurie testuoja tik patvirtinti_apmokejima funkcijos veikimą, todėl jums reikės mockinti patikrinti likutį funkcijos veikimą.

def patvirtinti_apmokejima(saskaitos_numeris, suma):
    saskaitos = {
        'LT5555': 300,
        'LT6666': 2654,
        'LT7777': 954876
    }
    if saskaitos[f'{saskaitos_numeris}'] >= suma:
        return True
    return False

def patvirtinti_apmokejima_ar_yra(saskaitos_numeris, suma):
    pakanka = patvirtinti_apmokejima(saskaitos_numeris, suma)
    return f"Banko sąskaita {saskaitos_numeris} {'gali' if pakanka else 'negali'} atlikti mokėjimą"

# 2 užduotis
# Parašykite funkciją analizuoti_excel(failo_kelias), kuri nuskaito duomenis iš Excel failo ir juos analizuoja. Duomenys yra pateikti lentelės pavidalu, kur pirmoje eilutėje yra stulpelių pavadinimai, o kiekvienoje sekančioje eilutėje yra įrašyti duomenys.

# Funkcija turi atlikti šiuos veiksmus:

# Nuskaityti duomenis iš Excel failo, kurio kelias nurodytas parametre failo_kelias.
# Apskaičiuoti vidurkį kiekvienam stulpeliui, kuriame yra skaičiai.
# Grąžinti žodyną, kuriame stulpelių pavadinimai yra raktai, o vidurkiai yra atitinkamos reikšmės.
# Parašykite bent du testus funkcijai analizuoti_excel, kurie padengtų šiuos scenarijus:

# Tikrinamas vidurkis kiekvienam stulpeliui, kai yra duomenys.
# Tikrinamas atitinkamo klaidingo duomenų formato apdorojimas, kai yra neteisingi duomenys Excel faile.

# Norėdami nuskaityti duomenis iš Excel failo ir juos analizuoti, galite naudoti pandas biblioteką. Tačiau, užduoties dalyje, susijusioje su testais, turite naudoti mocking'ą, kad būtų simuliuojamas tikras failo skaitymas ir analizė.
# import pandas as pd

# def analizuoti_excel(failo_kelias):
#         duomenys = pd.read_excel(failo_kelias)
#         vidurkiai = duomenys.mean()
#         return vidurkiai.to_dict()
