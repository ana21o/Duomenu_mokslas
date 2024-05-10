import sqlite3
import datetime
# Jūsų užsakovas yra smulkus autoservisas, kuriam yra reikalinga registracijos sistema
# Autoservisas nori kaupti informaciją apie:

    # 1. Mechanikus:
        # 1. vardas
        # 2. pavardė
        # 3. el_paštas
        # 4. valandinis_atlyginimas
        # 5. specializacija (elektra/važiuoklė/variklis/kėbulai)

class Mechanikas:
    def __init__(self, vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija ):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas
        self.valandinis_atlyginimas = valandinis_atlyginimas
        self.specializacija = specializacija

    # 2. Klientus:
        # 1. vardas
        # 2. pavardė
        # 3. el_paštas

class Klientas:
    def __init__(self, vardas, pavarde, el_pastas, mechaniko_id):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas
        self.mechaniko_id = mechaniko_id

    # 3. Klientų automobilius:
        # 1. Valstybinis numeris
        # 2. Markė
        # 3. Modelis
        # 4. Savininkas

class Automobilis:
    def __init__(self, valstybinis_numeris, marke, modelis, savininkas):
        self.valstybinis_numeris = valstybinis_numeris
        self.marke = marke
        self.modelis = modelis
        self.savininkas = savininkas

    # 4. Remontus:
        # 1. kliento_id
        # 2. mechaniko_id
        # 3. darbo_pradzia
        # 4. darbo_pabaiga
        # 5. darbo kaina (darbo_pabaiga - darbo_pradzia) x mechaniko valandinis įkainis x 2 (autoserviso dalis)
        # 6. remonto_kategorija (elektra/važiuoklė/variklis/kėbulai)

class Remontas:
    def __init__(self, kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija):
        self.kliento_id = kliento_id
        self.mechaniko_id = mechaniko_id
        self.darbo_pradzia = darbo_pradzia
        self.darbo_pabaiga = darbo_pabaiga
        self.darbo_kaina = darbo_kaina
        self.remonto_kategorija = remonto_kategorija

# jums taip pat reikės lentelės autoservisas, kuriame bus laikoma visa informacija.

class Autoservisas:
    def __init__(self):
        self.conn = sqlite3.connect('autoservisas.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS mechanikai(
                            mechaniko_id INTEGER PRIMARY KEY,
                            vardas VARCHAR(50) NOT NULL,
                            pavarde VARCHAR(50) NOT NULL,
                            el_pastas TEXT,
                            valandinis_atlyginimas REAL,
                            specializacija TEXT)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS klientai(
                            kliento_id INTEGER PRIMARY KEY,
                            vardas VARCHAR(50) NOT NULL,
                            pavarde VARCHAR(50) NOT NULL,
                            el_pastas TEXT,
                            mechaniko_id INTEGER,
                            FOREIGN KEY(mechaniko_id) REFERENCES mechanikai(mechaniko_id))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS automobiliai(
                            automobilio_id INTEGER PRIMARY KEY,
                            valstybinis_numeris TEXT,
                            marke TEXT,
                            modelis TEXT,
                            kliento_id INTEGER,
                            FOREIGN KEY (kliento_id) REFERENCES klientai(kliento_id))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS remontas(
                            remonto_id INTEGER PRIMARY KEY,
                            kliento_id INTEGER,
                            mechaniko_id INTEGER,
                            darbo_pradzia DATETIME,
                            darbo_pabaiga DATETIME,
                            darbo_kaina REAL,
                            remonto_kategorija TEXT,
                            FOREIGN KEY(kliento_id) REFERENCES klientai(kliento_id),
                            FOREIGN KEY(mechaniko_id) REFERENCES mechanikai(mechaniko_id))""")
        self.conn.commit()
        

# turint šias žinias jums reikės sukurti sistemą, valdomą per terminalą, vartotojas įjungęs aplikaciją, gali pasirinkti šiuos žingsnius:

# 1. pridėti:
    # 1. mechaniką
    # 2. klientą
    # 3. kliento automobilį
    # 4. remontą

    def prideti_mechanika(self, vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija):
        mechanikas = Mechanikas(vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija)
        self.cursor.execute('INSERT INTO mechanikai(vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija) VALUES (?, ?, ?, ?, ?)', (vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija))
        self.conn.commit()
        return mechanikas
    
    def prideti_klienta(self, vardas, pavarde, el_pastas, mechaniko_id):
        klientas = Klientas(vardas, pavarde, el_pastas, mechaniko_id)
        self.cursor.execute('INSERT INTO klientai (vardas, pavarde, el_pastas, mechaniko_id) VALUES (?, ?, ?, ?)', (vardas, pavarde, el_pastas, mechaniko_id))
        self.conn.commit()
        return klientas
    
    def prideti_automobili(self, valstybinis_numeris, marke, modelis, kliento_id):
        automobilis = Automobilis(valstybinis_numeris, marke, modelis, kliento_id)
        self.cursor.execute('INSERT INTO automobiliai(valstybinis_numeris, marke, modelis, kliento_id) VALUES (?, ?, ?, ?)', (valstybinis_numeris, marke, modelis, kliento_id))
        self.conn.commit()
        return automobilis
    

    def prideti_remonta(self, kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga,  remonto_kategorija):
        darbo_pradzia = datetime.datetime.strptime(darbo_pradzia, '%Y-%m-%d %H:%M:%S')
        darbo_pabaiga = datetime.datetime.strptime(darbo_pabaiga, '%Y-%m-%d %H:%M:%S')
        darbo_laikas = (darbo_pabaiga - darbo_pradzia).total_seconds()/3600
        mechaniko_valandinis_ikainis = self.gauti_mechaniko_valandini_ikaini(mechaniko_id)
        darbo_kaina = darbo_laikas * mechaniko_valandinis_ikainis * 2

        remontas = Remontas(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija)
        self.cursor.execute('INSERT INTO remontas(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija) VALUES (?, ?, ?, ?, ?, ?)', (kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija))
        self.conn.commit()
        return remontas
    
    def gauti_mechaniko_valandini_ikaini(self, mechaniko_id):
        self.cursor.execute('SELECT valandinis_atlyginimas FROM mechanikai WHERE mechaniko_id = ?', (mechaniko_id,))
        valandinis_atlyginimas = self.cursor.fetchone()[0]
        return valandinis_atlyginimas if valandinis_atlyginimas else 0.0
    
    
# 2. parodyti visus:
    # 1. mechanikus
    # 2. klientus
    # 3. klientų automobilus
    # 4. remontus

    def perziureti_irasus(self, lentele):
        self.cursor.execute(f"SELECT * FROM {lentele}")
        rezultatu_sarasas = self.cursor.fetchall()
        print('Irasai pagal jusu uzklausa: ')
        for rezultatas in rezultatu_sarasas:
            print(rezultatas)

# papildomos užduotys, jas iškviesti reikia terminale nurodant veiksmo numerį/įvedant skaičių:

# patobulinkite funkciją, kuri prieš pridedant remontą patikrintų ar tuo metu, kai klientas pageidauja remontuoti automobilį yra laisvų automechanikų
    def ar_laisvas_mechanikas(self, darbo_pradzia, darbo_pabaiga):
        self.cursor.execute('SELECT COUNT(*) FROM remontas WHERE (darbo_pradzia BETWEEN ? AND ?) OR (darbo_pabaiga BETWEEN ? AND ?)', (darbo_pradzia, darbo_pabaiga, darbo_pradzia, darbo_pabaiga))
        laisvu_mechaniku_skaicius = self.cursor.fetchone()[0]
        if laisvu_mechaniku_skaicius > 0:
            return True
        else:
            return False

# sukurkite funkciją, kuri apskaičiuotų, kiek vienas klientas yra mums sumokėjęs iš viso už visų savo automobilių visus remontus
# sukurkite funkciją, kuri apskaičiuotų, kiek vienas klientas yra mums sumokėjęs iš viso už vieno konkretaus automobilio remontą
# sukurkite funkciją, kuri apskaičiuotų kiek uždirbo konkretus mechanikas X
