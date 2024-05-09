import sqlite3

class Gyvunas:
    def __init__(self, vardas, amzius, svoris):
        self.vardas = vardas
        self.amzius = amzius
        self.svoris = svoris

class Prieglauda:
    def __init__(self):
        self.gyvunu_sarasas = []

    def prideti_gyvuna(self, gyvunas):
        self.gyvunu_sarasas.append(gyvunas)
    
    def istrinti_gyvuna(self, vardas):
        neistrinti = []
        for gyvunas in self.gyvunu_sarasas:
            if vardas != gyvunas.vardas:
                neistrinti.append(gyvunas)
        self.gyvunu_sarasas = neistrinti

# sukurti metodą, kuris grąžintų gyvūno objektą, kurio amžius yra lygus jūsų nurodytam amžiui
    def grazinti_objekta(self, amzius):
        for gyvunas in self.gyvunu_sarasas:
            if gyvunas.amzius == amzius:
                return gyvunas



gyvunai = [{'vardas':'Brisius', 'amzius': 10}, {'vardas':'kate', 'amzius': 5}]

prieglauda1 = Prieglauda()
prieglauda2 = Prieglauda()

gyvunas1 = Gyvunas('Testis', 4, 2)
gyvunas2 = Gyvunas('Brisius', 12, 25)


prieglauda1.prideti_gyvuna(gyvunas1)
prieglauda1.prideti_gyvuna(gyvunas2)
prieglauda1.istrinti_gyvuna('Testis')
# print(prieglauda1.gyvunu_sarasas)
rezultatas = prieglauda1.grazinti_objekta(12)
if rezultatas:
    print("Gyvuno vardas:", rezultatas.vardas)
else: 
    ("Tokio amžiaus gyvuno nera")


gyvunas3 = {
    "vardas": "kazkas",
    "amzius": 5,
    "svoris": 10
}

prieglauda1.gyvunu_sarasas.append(gyvunas1)
# prieglauda1.gyvunu_sarasas.append(gyvunas2)
# prieglauda1.gyvunu_sarasas.append(gyvunas3)

print('-----------------------')
for gyvunas in prieglauda1.gyvunu_sarasas:
    print(gyvunas.vardas)
print('-----------------------')

# print(gyvunas1.vardas)



class Motociklas:
    def __init__(self, marke, modelis, metai):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai

    def uzkurti(self):
        print(f"motociklas {self.marke} {self.modelis} buvo uzkurtas.")

motociklas1 = Motociklas('KTM', 'EXC450', 2016)
print(motociklas1.marke)
print(motociklas1.modelis)
print(motociklas1.metai)

motociklas1.uzkurti()

motociklas2 = Motociklas('Suzuki', 'DZR400', 2006)
motociklas2.uzkurti()

motociklas = {'marke': "Honda", 'modelis': 'CRF250', 'metai': 2018}
print(motociklas['modelis'])

print(type(motociklas))
zodis = 'labas'
print(type(zodis))
zodis = zodis.upper()
print(zodis)

skaicius = 5
print(type(skaicius))

print(type(motociklas1))



tv_kanalai = [
    {"padavinimas": "LRT", "programos": [{"savaites_diena": 1, "laidos": [{"laikas": "8:00", "pavadinimas": "Gustavo Enciklopedija", "dalyviai": [{"vardas": "Gustavas"}]}]}]}
]

print(tv_kanalai[0]['programos'][0]['laidos'][0]['dalyviai'][0]['vardas'])

print(prieglauda1.gyvunu_sarasas[0].vardas)
print(type(prieglauda1.gyvunu_sarasas[0].vardas))

print('----------------')
# sukurti klase baznycia (kunigo vardas, adresas, statybos metai)
# sukurti klase Vyskupija viena property - baznyciu_sarasas
# sukurti viena Vyskupija
# sukurti kelias baznycias


class Baznycia:
    def __init__(self, kunigo_vardas, adresas, statybos_metai, vyskupijos_id):
        self.kunigo_vardas = kunigo_vardas
        self.adresas = adresas
        self.statybos_metai = statybos_metai
        self.vyskupijos_id = vyskupijos_id

class Vyskupija:
    def __init__(self):
        self.baznyciu_sarasas = []
    
        self.conn = sqlite3.connect('vyskupija.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS vyskupija(
                            vyskupijos_id INTEGER PRIMARY KEY,
                            pavadinimas TEXT)""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS baznycia(
                            baznycios_id INTEGER PRIMARY KEY,
                            kunigo_vardas VARCHAR(50) NOT NULL,
                            adresas TEXT,
                            statybos_metai TEXT,
                            vyskupijos_id INTEGER,
                            FOREIGN KEY(vyskupijos_id) REFERENCES vyskupija(vyskupijos_id))""")
        
        # self.cursor.execute("INSERT INTO vyskupija (pavadinimas) VALUES ('katedra')")
        self.conn.commit()       

    # def prideti_baznycia(self, baznycia):
    #     self.cursor.execute("INSERT INTO baznycia (kunigo_vardas, adresas, statybos_metai, vyskupijos_id) VALUES (?, ?, ?, ?)", (baznycia.kunigo_vardas, baznycia.adresas, baznycia.statybos_metai, baznycia.vyskupijos_id))
        # self.baznyciu_sarasas.append(baznycia)

        self.conn.commit()
    
    def __del__(self):
        self.conn.close()

    def spausdinam_vyskupija(self):
        self.cursor.execute('SELECT * FROM vyskupija')
        vyskupijos = self.cursor.fetchall()
        print('----Vyskupija----')
        for baznycia in vyskupijos:
            print(baznycia)
    
    def spausdinam_baznycia(self):
        self.cursor.execute('SELECT * FROM baznycia')
        baznycios = self.cursor.fetchall()
        print('----Baznycia----')
        for baznycia in baznycios:
            print(baznycia)

    def istrinti_baznycia(self, adresas):
        self.cursor.execute("DELETE FROM baznycia WHERE adresas = ?", (adresas,))
        self.conn.commit()

    def atnaujinti_baznycia(self):
        metai_nauji = input('Iveskite naujus baznycios statybos metus: ')
        baznycios_id = input('Iveskite id')
        self.cursor.execute("UPDATE baznycia SET statybos_metai= ? WHERE baznycios_id = ? " , (metai_nauji, baznycios_id))
        self.conn.commit()


vyskupija = Vyskupija()

baznycia1 = Baznycia('Vytautas', 'Gedimino pr. 1', 1925, 1)
baznycia2 = Baznycia('Kazimieras', 'Stiklių g. 4,', 1832, 1)
baznycia3 = Baznycia('Rokas','Sirvydo g. 4', 1765, 1)

# vyskupija.prideti_baznycia(baznycia1)
# vyskupija.prideti_baznycia(baznycia2)
# vyskupija.prideti_baznycia(baznycia3)

vyskupija.spausdinam_vyskupija()
vyskupija.spausdinam_baznycia()

# istrinti baznycia, kuri leis istrinti baznycia pagal adresa, adresa turite pateikti kaip argumenta
print('-----Po trinimo-----')
vyskupija.istrinti_baznycia('Gedimino pr. 1')
vyskupija.spausdinam_baznycia()

print('---atnaujinta--')
vyskupija.atnaujinti_baznycia()


# print(vyskupija.baznyciu_sarasas[0].adresas)
# print(vyskupija.baznyciu_sarasas[2].adresas)



# sukurti metoda, kuris leis atnaujinti informacija vienai baznyciai, naudokite input


