# main.py

import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo
modelo = joblib.load("model/breast_cancer_model.pkl")

# Título de la app
st.title("🧠 Clasificador de Cáncer de Mama")

st.markdown("Introduce los valores para predecir si el tumor es **Benigno** o **Maligno**.")

# Inputs del usuario
radius_mean = st.number_input("Radio (mean)", min_value=0.0)
texture_mean = st.number_input("Textura (mean)", min_value=0.0)
perimeter_mean = st.number_input("Perímetro (mean)", min_value=0.0)
area_mean = st.number_input("Área (mean)", min_value=0.0)
smoothness_mean = st.number_input("Suavidad (mean)", min_value=0.0)

# Cuando el usuario hace clic en el botón
if st.button("Predecir"):
    entrada = pd.DataFrame([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean]],
                           columns=["mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness"])

    pred = modelo.predict(entrada)[0]
    resultado = "Maligno" if pred == 0 else "Benigno"

    st.subheader("Resultado:")
    st.write(f"🔍 El tumor es: **{resultado}**")
