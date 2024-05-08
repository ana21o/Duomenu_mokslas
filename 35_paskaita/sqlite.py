import sqlite3

# prisijungiame prie duomenu bazes
conn = sqlite3.connect('duomenu_baze.db')

# sukuriame objekta, kuris leis vikdyti uzduotis

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS zmones
#                (id INTEGER PRIMARY KEY, 
#                vardas TEXT,
#                amzius INTEGER)''')

# # cursor.execute("INSERT INTO zmones(vardas, amzius) VALUES (?, ?)", ('Jonas', 30))
# # cursor.execute("INSERT INTO zmones(vardas, amzius) VALUES (?, ?)", ('Petras', 40))
# # cursor.execute("INSERT INTO zmones(vardas, amzius) VALUES (?, ?)", ('Ona', 20))

# cursor.execute('SELECT * FROM zmones')
# rezultatai = cursor.fetchall()
# print(type(rezultatai))
# for zmogus in rezultatai:
#     print(zmogus)

# cursor.execute('SELECT * FROM zmones WHERE amzius > 25')
# rezultatai = cursor.fetchall()
# print('---------------------')
# for zmogus in rezultatai:
#     print(zmogus)

# # tokia pati uzklausa, tik yra naudojami kintamieji
# amzius = 25
# cursor.execute(f'SELECT * FROM zmones WHERE amzius > {amzius}')
# rezultatai = cursor.fetchall()
# print('---------------------')
# for zmogus in rezultatai:
#     print(zmogus)

# # vel tas pats, taciau dazniau naudojamas butent su uzklausomis
# cursor.execute(f"SELECT * FROM zmones WHERE amzius > ?", (25,))
# rezultatai = cursor.fetchall()
# print('---------------------')
# for zmogus in rezultatai:
#     print(zmogus)

# cursor.execute("UPDATE zmones SET amzius = ? WHERE vardas = ?", (31, 'Jonas'))
# cursor.execute(f"SELECT * FROM zmones WHERE amzius > ?", (25,))
# rezultatai = cursor.fetchall()
# print('---------------------')
# for zmogus in rezultatai:
#     print(zmogus)


# ka_istrinti = input('Iveskite varda, kuri norite istrinti: ')
# cursor.execute("DELETE FROM zmones WHERE vardas = ?", (ka_istrinti,))
# cursor.execute(f"DELETE FROM zmones WHERE vardas = {ka_istrinti}")

# cursor.execute("UPDATE zmones SET amzius = ? WHERE vardas = ?", (31, 'Jonas'))
# cursor.execute(f"SELECT * FROM zmones WHERE amzius > ?", (25,))
# rezultatai = cursor.fetchall()
# print('---------------------')
# for zmogus in rezultatai:
#     print(zmogus)



conn.commit()
conn.close()


