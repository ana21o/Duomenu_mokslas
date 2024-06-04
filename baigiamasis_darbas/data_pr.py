import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import joblib

df = pd.read_csv('mobile_autoplius.csv', sep=';')
df['metai'] = df['metai'].astype(int)
df['kaina'] = df['kaina'].str.replace('€', '').str.replace(' ', '').astype(float)

df['rida'] = df['rida'].apply(lambda x: x.replace('km', '').replace(' ', '') if 'km' in x else 'Nenurodyta')
df['rida'] = pd.to_numeric(df['rida'], errors='coerce')

df['kW'] = df['variklis'].str.extract(r'(\d+)kW')[0]
df['kW'] = pd.to_numeric(df['kW'], errors='coerce')

df.dropna(subset=['rida', 'kW', 'kaina', 'kuras', 'pavaros'], inplace=True)

# Kategorinių reikšmių paverčiamos skaitinėmis reprezentacijomis stulpelyje 'kuras'
df['kuras'] = df['kuras'].map({
    'Benzinas': 0, 
    'Dyzelinas': 1, 
    'Elektra': 2, 
    'Benzinas / elektra': 3, 
    'Dyzelinas / elektra': 4, 
    'Benzinas / dujos': 5
})
# Tuščios reikšmės stulpelyje 'kuras' užpildomos -1 ir paverčiamos sveikaisiais skaičiais
df['kuras'] = df['kuras'].fillna(-1).astype(int)

# Kategorinių reikšmių paverčiamos skaitinėmis reprezentacijomis stulpelyje 'pavaros'
df['pavaros'] = df['pavaros'].map({
    'Mechaninė': 0, 
    'Automatinė': 1
})

X = df[['metai', 'rida', 'kW', 'kuras', 'pavaros']]
y = df['kaina']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    'Linear Regression':
LinearRegression(),
    'Polynomial Regression':
make_pipeline(PolynomialFeatures(degree=2), Ridge()),
    'Decision Tree':
DecisionTreeRegressor(),
    'Random Forest':
RandomForestRegressor()
}

param_grids = {
'Polynomial Regression': {
    'ridge__alpha': [0.1, 1.0, 10.0]
},
'Decision Tree': {
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
},
'Random Forest': {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]}}

results = {}

for name, model in models.items():
    if name in param_grids:
        grid_search = GridSearchCV(model, param_grids[name], cv=5, scoring='neg_mean_squared_error')
        grid_search.fit(X_train_scaled, y_train)
        best_model = grid_search.best_estimator_
    else:
        best_model = model
        best_model.fit(X_train_scaled, y_train)
    
    y_pred = best_model.predict(X_test_scaled)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    results[name] = {'RMSE': rmse, 'R2': r2}
    print(f'{name}: RMSE={rmse}, R2 = {r2}')

# Išsaugoti geriausią modelį po ciklo
joblib.dump(best_model, 'best_model2.pkl')
    

plt.figure(figsize=(10, 5))

# Sukuriamas RMSE ir R^2 rezultatų sąrašai
rmse_values = [results[model]['RMSE'] for model in results]
r2_values = [results[model]['R2'] for model in results]

# Piešiama juostinė diagrama
plt.bar(results.keys(), rmse_values, label = 'RMSE')
plt.bar(results.keys(), r2_values, bottom=rmse_values, label='R2')

# Papildomi diagramos nustatymai
plt.xlabel('Modelis')
plt.ylabel('Rezultatai')
plt.title('Modeliu palyginimas')
plt.legend()

# Rodyti diagramą
plt.show()




class CarPricePredictor:
    def __init__(self, model):
        self.model = model
    
    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
    