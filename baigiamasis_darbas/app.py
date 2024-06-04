from data_pr import CarPricePredictor
import sqlite3
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

class CarPriceApp:
    def __init__(self, db_path= 'car_prices.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()
        self.model = joblib.load('best_model.pkl')

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS user_inputs (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       metai INTEGER,
                       rida INTEGER,
                       kW INTEGER,
                       kuras INTEGER,
                       pavaros INTEGER,
                       predicted_price REAL)''')
        self.conn.commit()

    def predict_and_store(self, metai, rida, kW, kuras, pavaros):
        input_data = np.array([[metai, rida, kW, kuras, pavaros]])
        input_data_scaled = scaler.transform(input_data)
        predicted_price = self.model.predict(input_data_scaled)[0]
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO user_inputs (metai, rida, kW, kuras, pavaros, predicted_price)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (metai, rida, kW, kuras, pavaros, predicted_price))
        self.conn.commit()
        return predicted_price

app = CarPriceApp()
predicted_price = app.predict_and_store(2015, 100000, 110, 0, 1)  # Пример с числовыми значениями категорий
print(f'Predicted price: {predicted_price}')
