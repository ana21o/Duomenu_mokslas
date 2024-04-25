class Receptas:
    def __init__(self, pavadinimas, ruosimo_laikas, ingredientu_sarasas):
        self.pavadinimas = pavadinimas
        self.ruosimo_laikas = ruosimo_laikas
        self.ingredientu_sarasas = ingredientu_sarasas

class ReceptuValdymas:
    def __init__(self):
        self.receptai = []

    def gauti_pavadinimus(self):
        return [receptas.pavadinimas for receptas in self.receptai]

    def prideti_recepta(self, receptas):
        self.receptai.append(receptas)

    def gauti_receptus_pagal_laika(self, maksimalus_laikas):
        return [receptas for receptas in self.receptai if receptas.ruosimo_laikas <= maksimalus_laikas]
    
    def atrinkti_pagal_ingredientus(self, ingredientas):
        atrinkti = []
        for receptas in self.receptai:
            for produktas in receptas.ingredientu_sarasas:
                if produktas == ingredientas:
                    atrinkti.append(receptas)
                    break
        return atrinkti


# 1 užduotis
# papildykite klasę ReceptųValdymas pridedant metodą pasalinti_recepta, šis metodas turi panaikinti receptą iš receptų sąrašo,
# pagal pateiktą pavadinimą
# parašykite testą, kad įsitikintumėte ar jūsų metodas veikia tinkamai

    def pasalinti_recepta(self, pavadinimas):
        self.receptai = [receptas for receptas in self.receptai if receptas.pavadinimas != pavadinimas]
        # rezultatai = []
        # for receptas in self.receptai:
        #     if receptas.pavadinimas != pavadinimas:
        #         rezultatai.append()
        # self.receptai = rezultatai

# 2 užduotis
# Sukurkite metodą gauti_receptus_pagal_zodi(), kuris grąžina sąrašą receptų, kurių pavadinimuose yra nurodytas žodis.
# patikrinkite ar metodas veikia tinkamai, parašydami unit testą

    def gauti_receptus_pagal_zodi(self, zodis):
        return [receptas.pavadinimas for receptas in self.receptai if zodis.lower() in receptas.pavadinimas.lower()]

# 3 užduotis
# Sukurkite metodą gauti_bendra_ruosimo_laika(), kuris grąžina visų receptų bendrą ruošimo laiką.
# patikrinkite ar metodas veikia tinkamai, parašydami unit testą

    def gauti_bendra_ruosimo_laika(self):
        return sum(receptas.ruosimo_laikas for receptas in self.receptai)
        
# 4 užduotis
# Pridėkite metodą isvalyti_receptus(), kuris išvalytų visus receptus iš sąrašo.
# patikrinkite ar metodas veikia tinkamai, parašydami unit testą

    def isvalyti_receptus(self):
        self.receptai = []



    # def atnaujinti_paruosimo_laika(self, naujas_laikas=20, pavadinimas = 'arbata'):
    #     for receptas in self.receptai:
    #        if receptas.pavadinimas == pavadinimas:
    #            receptas.paruosimo_laikas = naujas_laikas



