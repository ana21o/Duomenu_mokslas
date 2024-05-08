import sqlite3

class Gydytojas:
    def __ini__(self, vardas, pavarde, specializacija, el_pastas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.specializacija = specializacija
        self.el_pastas = el_pastas

class Pacientas:
    def __init__(self, vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.lytis = lytis
        self.el_pastas = el_pastas
        self.gydytojo_id = gydytojo_id

class Susitikimas:
    def __init__(self, paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai):
        self.paciento_id = paciento_id
        self.gydytojo_id = gydytojo_id
        self.susitikimo_data = susitikimo_data
        self.paskirtis = paskirtis
        self.komentarai = komentarai

class Ligonine:
    def __init_(self):
        self.conn = sqlite3.connect('ligonine.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS gydytojai(
                gydytojo_id INTEGER PRIMARY KEY,
                vardas VARCHAR(50) NOT NULL,
                pavarde VARCHAR(50) NOT NULL,
                specilizacija VARCHAR(50) NOT NULL,
                el_pastas TEXT)""")
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS pacientai(
                paciento_ID INTEGER PRIMARY KEY,
                vardas VARCHAR(50) NOT NULL,
                pavarde VARCHAR(50) NOT NULL,
                gimimo_data TEXT,
                lytis VARCHAR(15),
                el_pastas TEXT,
                gydytojo_id INTEGER,
                FOREIGN KEY (gydytojo_id) REFERENCES gydytojai(gydytojo_id))""")
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS susitikimai(
                susitikimo_id INTEGER PRIMARY KEY,
                paciento_ID INTEGER,
                gydytojo_id INTEGER,
                data_laikas TEXT,
                susitikimo_paskirtis TEXT,
                komentarai_pastabos TEXT,
                FOREIGN KEY (paciento_ID) REFERENCES pacientai(paciento_ID),
                FOREIGN KEY (gydytojo_id) REFERENCES gydytojai(gydytojo_id)""")
        
    def prideti_gydytoja(self, vardas, pavarde, specializacija, el_pastas):
        gydytojas = Gydytojas(vardas, pavarde, specializacija, el_pastas)
        self.cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", (vardas, pavarde, specializacija, el_pastas))
        self.conn.commit()
        return gydytojas
    
    def prideti_pacienta(self, vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id):
        pacientas = Pacientas(vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id)
        self.cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id))
        self.conn.commit()
        return pacientas