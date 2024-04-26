from datetime import datetime

class Gyvunas:
    def __init__(self, metai, rusis, vardas, svoris):
        self.gimimo_metai = metai  
        self.rusis = rusis
        self.vardas = vardas
        self.svoris = svoris
        self.amzius = self.apskaiciuoti_amziu(metai)

    def apskaiciuoti_amziu(self, metai):
        today = datetime.now()
        return today.year - metai
    
class GyvunuPrieglauda:
    def __init__(self, pavadinimas):
        self.gyvunai = []
        self.pavadinimas = pavadinimas

    def prideti_gyvuna(self, gyvunas):
        self.gyvunai.append(gyvunas)

    # gauti pagal rusi, svori

    def gauti_pagal_rusi(self, rusis):
        # return [gyvunas for gyvunas in self.gyvunai if gyvunas.rusis == rusis]
        gyvunai = []
        for gyvunas in self.gyvunai:
            if gyvunas.rusis == rusis:
                gyvunai.append(gyvunas)
        return gyvunai
    
    def gauti_pagal_svoris(self, svoris):
        return [gyvunas for gyvunas in self.gyvunai if gyvunas.svoris == svoris]

gyvunas1 = Gyvunas(2015, 'suo', 'Reksas', 20)
prieglauda1 = GyvunuPrieglauda('Lese')
prieglauda2 = GyvunuPrieglauda('Reksas')


prieglauda1.prideti_gyvuna(gyvunas1)
prieglauda1.prideti_gyvuna(Gyvunas(2020, 'kate', 'Test', 3))
print(prieglauda1.gyvunai[0].vardas)
gyvunai = prieglauda1.gauti_pagal_rusi('suo')
print(gyvunai)

    



# Ši užduotis yra papildoma! jos spręsti nėra privaloma!

# Sukurkite klasę Gyvūnas, suteikite jai keletą properties (amzius, rusis, vardas, svoris arba savo nuožiūra)
# Sukurkite antrą klasę GyvūnųPrieglauda
# Ši klasė turi turėti metodus pridėti naujus gyvūnus, taip pat gauti gyvūnus gal rūšį (pvz. matyti tik kates), pagal svorį
# Parašykite testų, kurie užtikrintų, kad jūsų funkcija veikia tinkamai