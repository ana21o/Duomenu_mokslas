import pandas as pd 
import sqlite3
import joblib
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from car_price_predictor import CarPricePredictor
from database import create_table, insert_user_input, fetch_all_data, delete_user_input
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Modelio ir skalės įkėlimas
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Duomenų bazės lentelės kūrimas
create_table()

# Pagrindinio meniu funkcija
def main_menu():
    print('--------------------')
    print("Pasirinkite veiksmą:")
    print('--------------------')
    print("1. Įvesti automobilio duomenis ir prognozuoti kainą")
    print('--------------------')
    print("2. Peržiūrėti visus įrašus duomenų bazėje")
    print('--------------------')
    print("3. Ištrinti įrašą iš duomenų bazės")
    print('--------------------')
    print("4. Išeiti iš programos")

# Gamyntojų sarašas
gamintojai = {0:'BMW', 1:'Skoda', 2:'Audi', 3:'Volkswagen', 4:'Peugeot', 5:'Volvo', 6:'Mercedes-Benz', 7:'Subaru', 8:'Toyota', 9:'Land Rover', 10:'Jaguar', 11:'Alfa Romeo', 12:'Opel', 13:'Honda', 14:'Nissan', 15:'Suzuki', 16:'Kia', 17:'Chevrolet', 18:'Hyundai', 19:'Infiniti', 20:'Renault', 21:'Citroen', 22:'Chrysler', 23:'Mitsubishi', 24:'Maserati', 25:'Porsche', 26:'Ford', 27:'Mazda', 28:'Lexus', 29:'Seat', 30:'Tesla', 31:'Jeep', 32:'Lancia', 33:'Moskvich', 34:'Fiat', 35:'Smart', 36:'Mini', 37:'Daihatsu', 38:'Pontiac', 39:'Dacia', 40:'Saab', 41:'Dodge', 42:'SsangYong', 43:'DR', 44:'Iveco', 45:'Cadillac', 46:'Aixam', 47:'Microcar', 48:'DS', 49:'Ligier'}

def input_manufacturer():
    while True:
        try: 
            print("nĮveskite automobilio duomenis: ")
            for key, value in gamintojai.items():
                    print(f"{key}: {value}")
            gamintojas = int(input('Pasirinkite markę (numeris): '))
            if gamintojas not in gamintojai:
                    raise ValueError("Neteisingas markės numeris. Pasirinkite iš sąrašo.")    
            return gamintojas
        except ValueError as e:
            print(e)

def input_year():
    while True:
        try:
            metai = int(input('Metai: '))
            if metai < 1900 or metai > 2024:  # Patikrinimas, ar metai tinkami
                raise ValueError("Netinkami metai. Įveskite metus nuo 1900 iki 2024.")
            return metai
        except ValueError as e:
            print(e)

def input_mileage():
    while True:
        try:
            rida = float(input('Rida (km): '))
            if rida < 0:
                raise ValueError("Neteisinga rida. Įveskite teigiamą skaičių.")
            return rida
        except ValueError as e:
            print(e)

def input_engine_power():
    while True:
        try:
            kW = float(input('Variklio galia (kW): '))
            return kW
        except ValueError as e:
            print(e)

def input_fuel():
    while True:
        try:
            print('\nKuras: ')
            print("0: Benzinas, 1: Dyzelinas, 2: Elektra, 3: Benzinas / elektra, 4: Dyzelinas / elektra, 5: Benzinas / dujos")
            kuras = int(input('Pasirinkite kura (numeris): '))
            if kuras not in [0, 1, 2, 3, 4, 5]:
                raise ValueError("Neteisingas kuro numeris. Pasirinkite iš sąrašo.")
            return kuras
        except ValueError as e:
            print(e)
                    
def input_transmission():
    while True:
        try:
            print('\nPavarų dėžė: ')
            print("0: Mechaninė, 1: Automatinė")
            pavaros = int(input('Pasirinkite pavaru deze (numeris): '))
            if pavaros not in [0, 1]:
                raise ValueError("Neteisingas pavaru deze numeris. Pasirinkite iš sąrašo.")
            return pavaros
        except ValueError as e:
            print(e)

# Vartotojo duomenų įvedimo funkcija
def input_data():
    gamintojas = input_manufacturer()
    metai = input_year()
    rida = input_mileage()
    kW = input_engine_power()
    kuras = input_fuel()
    pavaros = input_transmission()
    return gamintojas, metai, rida, kW, kuras, pavaros

# Automobilių su panašiomis kainomis paieškos funkcija
def find_matching_cars(predicted_price, df):
# Filtruoti automobilius, kurių kainos yra ±500 EUR nuo prognozuojamos kainos
        return df[(df['kaina'] <= predicted_price +500) & (df['kaina'] >= predicted_price -500)]

# Funkcija, kuri atvaizduoja grafiką su panašiais automobiliais ir jų kainomis
def plot_similar_cars(predicted_price, matching_cars, user_data):
    plt.figure(figsize=(10, 6))
    plt.scatter(matching_cars['rida'], matching_cars['kaina'], label= 'Panašūs automobiliai')
    plt.scatter(user_data['rida'], predicted_price, color='red', label='Jūsų automobilis')
    plt.xlabel('Rida (km)')
    plt.ylabel('Kaina (€)')
    plt.title('Automobilių kainų palyginimas')
    plt.legend()
    plt.grid(True)
    plt.show()

# Automobilio kainos prognozavimo funkcija
def predict_price():
    gamintojas, metai, rida, pavaros, kuras, kW = input_data()
    df = pd.read_csv('cleaned_mobile_autoplius.csv', sep=';')
    user_data = pd.DataFrame([[gamintojas, metai, rida, pavaros, kuras, kW]],
                             columns=['gamintojas', 'metai', 'rida', 'pavaros', 'kuras', 'kW'])
    user_data_scaled = scaler.transform(user_data)

# Prognozuoti automobilio kainą
    predicted_price = model.predict(user_data_scaled)[0]
    print(f"Prognozuojama automobilio kaina: {predicted_price:.2f} EUR")

    # Ieškoti markių pagal prognozuotą kainą 
    matching_cars = find_matching_cars(predicted_price, df)
    print("Automobiliai, kurių kainos yra artimos prognozuotoms:")
    for _, row in matching_cars.iterrows():
        print(f"{gamintojai[int(row['gamintojas'])]}: {row['kaina']} EUR")

    matching_prices = matching_cars['kaina']

    if len(matching_prices) > 0:
        prediction_accuracy = 1.0 - (abs(predicted_price - matching_prices.mean()) / matching_prices.mean())
        print(f'Prognozes tikslumas: {prediction_accuracy:.2%}')
    else:
        prediction_accuracy = 0.0
        print('Nerasta atitikmenų automobilių pagal kainą ±500 EUR intervale.')

# Įrašyti vartotojo duomenis į duomenų bazę
    insert_user_input(gamintojas, metai, rida, pavaros, kuras, kW, predicted_price, prediction_accuracy)

 # Sukurti ir parodyti grafiką
    plot_similar_cars(predicted_price, matching_cars, user_data.iloc[0])

# Duomenų bazės įrašų peržiūros funkcija
def view_database():
    data = fetch_all_data()
    print("\nVisi įrašai duomenų bazėje:")
    for row in data:
        print(row)

def delete_record():
    try:
        id_to_delete = int(input("Įveskite įrašo ID, kurį norite ištrinti: "))
        delete_user_input(id_to_delete)  # Kviečiame funkciją iš database.py, kad ištrintumėte įrašą
        print(f"Įrašas su ID {id_to_delete} sėkmingai ištrintas.")
    except ValueError:
        print('Neteisingas ID formatas.')
    except Exception as e:
        print(f"Klaida: {e}")

# Pagrindinė programa
def main():
    while True:
        main_menu()
        print('--------------------')
        choice = input("Pasirinkite veiksmą (1/2/3/4): ")
        if choice == '1':
            predict_price()
        elif choice == '2':
            view_database()
        elif choice == '3':
            delete_record()
        elif choice == '4':
            print('--------------------')
            print("Programa baigė darbą.")
            break
        else:
            print('--------------------')
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

if __name__ == "__main__":
    main()           






