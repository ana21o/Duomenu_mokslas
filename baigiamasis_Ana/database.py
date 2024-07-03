import sqlite3

def create_table():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_inputs(
              id INTEGER PRIMARY KEY,
              gamintojas TEXT,
              metai UNTEGER,
              rida REAL,
              kW REAL,
              kuras INTEGER, 
              pavaros INTEGER, 
              predicted_price REAL,
              prediction_accuracy REAL)''')
    conn.commit()
    conn.close()

def insert_user_input(gamintojas, metai, rida, kW, kuras, pavaros, predicted_price, prediction_accuracy):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO user_inputs(gamintojas, metai, rida, kW, kuras, pavaros, predicted_price, prediction_accuracy) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (gamintojas, metai, rida, kW, kuras, pavaros, predicted_price, prediction_accuracy))
    conn.commit()
    conn.close()

def delete_user_input(id):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("DELETE FROM user_inputs WHERE id=?", (id,))
    conn.commit()
    conn.close()

def fetch_all_data():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user_inputs")
    rows = c.fetchall() # Gauti visus rezultatus
    conn.close()
    return rows
