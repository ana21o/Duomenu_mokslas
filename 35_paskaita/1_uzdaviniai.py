import sqlite3
from datetime import datetime

conn = sqlite3.connect('duomenu_baze_uzdaviniai.db')

cursor = conn.cursor()

# 1. sukurkite duomenų bazę, kurioje turėtų būti šios lentelės: gydytojai, pacientai, susitikimai

# 1. Gydytojai:
    # ID (unikalus)
    # Vardas
    # Pavardė
    # Specializacija
    # Kontaktinė informacija (el. paštas)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS gydytojai(
               id INTEGER PRIMARY KEY,
               vardas VARCHAR(50) NOT NULL,
               pavarde VARCHAR(50) NOT NULL,
               specializacija TEXT,
               el_pastas TEXT)""")

# 2. Pacientai:
    # ID (unikalus)
    # Vardas
    # Pavardė
    # Gimimo data
    # Lytis
    # Kontaktinė informacija (el. paštas)
    # Gydytojo ID (susiejimas su gydytoju, pvz. šeimos gydytojas)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientai(
               id INTEGER PRIMARY KEY,
               vardas VARCHAR(50) NOT NULL,
               pavarde VARCHAR(50) NOT NULL,
               gimimo_data TEXT,
               lytis TEXT,
               el_pastas TEXT,
               gydytojo_id INTEGER,
               FOREIGN KEY(gydytojo_id) REFERENCES gydytojai(id))""")

# 3. Susitikimai:
    # ID
    # Paciento ID
    # Gydytojo ID
    # Susitikimo data ir laikas
    # Susitikimo paskirtis/arba diagnozė
    # Komentarai/arba pastabos

cursor.execute("""
    CREATE TABLE IF NOT EXISTS susitikimai(
               id INTEGER PRIMARY KEY,
               paciento_id INTEGER,
               gydytojo_id INTEGER,
               susitikimo_data_laikas DATETIME,
               paskirtis_arba_diagnoze TEXT,
               komentarai_arba_pastabos TEXT,
               FOREIGN KEY(paciento_id) REFERENCES pacientai(id),
               FOREIGN KEY(gydytojo_id) REFERENCES gydytojai(id))""")


# 2. Užpildykite šias lenteles duomenimis (bent 10 įrašų kiekvienai lentelei)

# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Jelena', 'Grigorjeva', 'seimos gydytojas', 'jelena@grigorjeva.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Edita', 'Miliene', 'seimos gydytojas', 'edita@miliene.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Andrius', 'Beliajevas', 'chirurgas', 'andrius@beliajevas.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Aiste', 'Riktere', 'chirurgas', 'aiste@riktere.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Saulius', 'Taroza', 'neurologas', 'saulius@taroza.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Gintaras', 'Kuprionis', 'endokrinologas', 'gintaras@kuprionis.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Evalda', 'Danyte', 'endokrinologas', 'evalda@danyte.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Jurgita', 'Zvikaite', 'akuseris', 'jurgita@zvukaite.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Veronika', 'Sobolevskaja', 'psihiatras', 'veronika@sobolevskaja.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, el_pastas) VALUES (?, ?, ?, ?)", ('Ruta', 'Stabuliene', 'neurologas', 'ruta@stabuliene.com'))

# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Petras', 'Petrauskas', '1978-05-12', 'vyras', 'petras@petrauskas.com', 1))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Rimas', 'Rimukas', '2002-07-02', 'vyras', 'rimas@rimukas.com', 2))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Ramune', 'Ramuniene', '1967-10-22', 'moteris', 'ramune@ramuniene.com', 3))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Tomas', 'Tomaitis', '1999-12-03', 'vyras', 'tomas@tomaitis.com', 4))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Rita', 'Ritaite', '1985-02-15', 'moteris', 'rita@ritaite.com', 5))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Adomas', 'Adomaitis', '1960-01-06', 'vyras', 'adomas@adomaitis.com', 6))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Jonas', 'Jonukas', '2001-02-14', 'vyras', 'jonas@jonukas.com', 7))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Jolanta', 'Jolantiene', '1995-05-19', 'moteris', 'jolanta@jolantiene.com', 8))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Andrius', 'Andraitis', '1985-03-07', 'vyras', 'andrius@andraitis.com', 9))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Paulius', 'Paulauskas', '1989-04-05', 'vyras', 'paulius@paulauskas.com', 10))

# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (1, 1, '2024-05-15 10:00:00', 'Rutininis patikrinimas', 'Pacientas pasijuto gerai'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (2, 2, '2023-02-12 11:30:00', 'Ligos diagnozė', 'Pacientė pranešė apie simptomus'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (3, 3, '2023-06-03 12:45:00', 'Operacija', 'Paciento sutikimas gautas'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (4, 4, '2022-12-12 15:15:00', 'Operacija', 'Pacientas pasiruošęs operacijai'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (5, 5, '2022-12-12 15:15:00', 'Konsultacija', 'Pacientė patenkinta gydymo rezultatais'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (6, 6, '2023-08-22 09:45:00', 'Ligos diagnozė', 'Gydytojas rekomendavo vaistus'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (7, 7, '2022-10-01 13:25:00', 'Konsultacija', 'Pacientė nori papildomo patarimo'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (8, 8, '2024-02-23 12:00:00', 'Rutininis patikrinimas', 'Pacientas pasijuto gerai'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (9, 9, '2023-10-15 14:50:00', 'Konsultacija', 'Pacientas atvyko laiku'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data_laikas, paskirtis_arba_diagnoze, komentarai_arba_pastabos) VALUES (?, ?, ?, ?, ?)", (10, 10, '2022-09-18 11:15:00', 'Ligos diagnozė', 'Gydytojas rekomendavo vaistus'))


cursor.execute("SELECT * FROM gydytojai")
gydytojai = cursor.fetchall()
for gydytojas in gydytojai:
    print(gydytojas)

print('------------------------')

cursor.execute("SELECT * FROM pacientai")
pacientai = cursor.fetchall()
for pacientas in pacientai:
    print(pacientas)

print('------------------------')

cursor.execute("SELECT * FROM susitikimai")
susitikimai = cursor.fetchall()
for susitikimas in susitikimai:
    print(susitikimas)

print('------------------------')



# 3. Atlikite šias užklausas:

    # 1. Visi pacientai, kurių gimimo data yra mažiau nei 1970-01-01 turėtų būti priskirti gydytojui, kurio ID yra 1

cursor.execute("UPDATE pacientai SET gydytojo_id = 1 WHERE gimimo_data < '1970-01-01'")
cursor.execute("SELECT * FROM pacientai")
pacientai = cursor.fetchall()
for pacientas in pacientai:
    print(pacientas)

print('------------------------')

    # 2. Raskite visus susitikimus, kurie vyksta šiandien. (rezultate norime matyti kliento vardą ir pavardę, gydytojo vardą ir pavardę ir susitikimo paskirtį)
siandienos_data = datetime.now().strftime('%Y-%m-%d')

cursor.execute("""
    SELECT pacientai.vardas, pacientai.pavarde, gydytojai.vardas, gydytojai.pavarde, susitikimai.paskirtis_arba_diagnoze
    FROM susitikimai
    INNER JOIN pacientai 
    ON susitikimai.paciento_id = pacientai.id
    INNER JOIN gydytojai
    ON susitikimai.gydytojo_id = gydytojai.id
    WHERE DATE(susitikimai.susitikimo_data_laikas) = ? """, (siandienos_data,))

susitikimai = cursor.fetchall()
if susitikimai:
    for susitikimas in susitikimai:
        print(susitikimas)
else:
    print('Šiandien nėra susitikimų')

print('------------------------')

    # 3. Sukurkite užklausą, kuri ištrintų visus susitikimus, kurie įvyko daugiau nei 6 mėnesiai nuo šiandienos datos.

cursor.execute("DELETE FROM susitikimai WHERE DATE(susitikimo_data_laikas) < date('now', '-6 month')")
cursor.execute("SELECT * FROM susitikimai")
susitikimai = cursor.fetchall()
for susitikimas in susitikimai:
    print(susitikimas)

print('------------------------')

    # 4. Parašykite užklausą, kuri rastų gydytojų vardus ir pavardes, kuriems yra priskirti pacientai, kurių susitikimo paskirtyje yra žodis "trauma"

cursor.execute("""
    SELECT gydytojai.vardas, gydytojai.pavarde
    FROM gydytojai
    JOIN susitikimai
    ON gydytojai.id = susitikimai.gydytojo_id
    JOIN pacientai 
    ON pacientai.id = susitikimai.paciento_id
    WHERE susitikimai.paskirtis_arba_diagnoze LIKE '%trauma%'
""")

gydytojai = cursor.fetchall()
if gydytojai:
    for gydytojas in gydytojai:
        print(gydytojai)
else:
    print('Nėra gydytojų su susitikimais, kuriuose yra diagnozė „trauma“')

print('------------------------')

    # 5. Raskite visus pacientus, kurių gydytojo specializacija yra chirurgija ir susitikimo paskirtis yra operacija.

cursor.execute("""
    SELECT pacientai.vardas, pacientai.pavarde
    FROM pacientai
    JOIN susitikimai
    ON pacientai.id = susitikimai.paciento_id
    JOIN gydytojai
    ON gydytojai.id = susitikimai.gydytojo_id
    WHERE gydytojai.specializacija = 'chirurgas' AND susitikimai.paskirtis_arba_diagnoze = 'Operacija'
""")

pacientai = cursor.fetchall()
if pacientai:
    for pacientas in pacientai:
        print(pacientai)
else:
    print('Tokiu pacientų nėra')

conn.commit()
conn.close()
