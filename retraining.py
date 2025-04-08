# retraining.py

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Crear carpeta para el modelo si no existe
os.makedirs("model", exist_ok=True)

# Cargar dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(modelo, "model/breast_cancer_model.pkl")

print("✅ Modelo entrenado y guardado en 'model/breast_cancer_model.pkl'")
