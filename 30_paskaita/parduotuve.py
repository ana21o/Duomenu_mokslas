class Preke:
    def __init__(self, pavadinimas, kaina, kiekis):
        self.pavadinimas = pavadinimas
        self.kaina = float(kaina)
        self.kiekis = int(kiekis)
    
    def __str__(self):
        return f"{self.pavadinimas} | {self.kaina} | {self.kiekis}"

class Parduotuve:
    def __init__(self):
        self.prekes = []
        self.nuskaitytas = False

    def prideti_preke(self, preke):
        self.prekes.append(preke)

    def perziureti_prekes(self):
        if self.prekes:
            print('Parduotuves prekes:')
            for index, preke in enumerate(self.prekes):
                print(f"{index} - {preke}")
        else:
            print('Prekiu nera')

    def gauti_preke_pagal_index(self, prekes_index):
        for index, preke in enumerate(self.prekes):
            if index == int(prekes_index):
                return preke
        # return self.prekes[prekes_index]

    def istrinti_preke(self, prekes_index):
        naujos_prekes = []
        for index, preke in enumerate(self.prekes):
            if index != int(prekes_index):
                naujos_prekes.append(preke)
        self.prekes = naujos_prekes

    def rikiuoti_pagal_savybe(self, rikiuoti_pagal):
        # galima prideti kuria kryptimi rikiuoti
        if rikiuoti_pagal == 'pavadinimas':
            rikiuotos_prekes = sorted(self.prekes, key=lambda preke: preke.pavadinimas)
        elif rikiuoti_pagal == 'kaina':
            rikiuotos_prekes = sorted(self.prekes, key=lambda preke: preke.kaina)
        else:
            rikiuotos_prekes = sorted(self.prekes, key=lambda preke: preke.kiekis)
        return [preke.__str__() for preke in rikiuotos_prekes]
        # return [f"{preke.pavadinimas} | {preke.kaina} | {preke.kiekis}" for preke in rikiuotos_prekes]

    def atnaujinti_preke(self, prekes_index, atnaujinta_preke):
        preke = self.gauti_preke_pagal_index(prekes_index)
        if preke:
            preke.pavadinimas = atnaujinta_preke.pavadinimas
            preke.kaina = atnaujinta_preke.kaina
            preke.kiekis = atnaujinta_preke.kiekis
            print('Preke atnaujinta sekmingai!')
        else:
            print('Tokia preke neegzistuoja!')






# def suma(a,b):
#     return a+b

# suma_lambda = lambda a,b: a+b

# suma_lambda(5,10)

# [{'kaina': 50, 'pavadinimas': 'test'}, {'kaina': 20, 'pavadinimas': 'test2'}]
# [50,20]