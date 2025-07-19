# streamlit_prediccion_vuelos.py
import streamlit as st
import pandas as pd
import cloudpickle

# Cargar modelo directamente desde archivo local
with open("modelo_knn_pipeline.pkl", "rb") as f:
    model = cloudpickle.load(f)

# Configuración de la app
st.set_page_config(page_title="¿Se va a demorar mi vuelo?", layout="centered")
st.title("✈️ Predicción de Demoras de Vuelo con KNN")
st.markdown("Complete la información del vuelo para predecir si se espera una demora mayor a 15 minutos.")

# Formulario de entrada
month = st.selectbox("Mes", list(range(1, 13)))
day_of_week = st.selectbox("Día de la semana", [1, 2, 3, 4, 5, 6, 7], format_func=lambda x: ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"][x-1])
latitude = st.number_input("Latitud", value=40.6)
longitude = st.number_input("Longitud", value=-73.8)
prcp = st.number_input("Precipitación (PRCP)", value=0.0)
dep_time_blk = st.selectbox("Bloque horario de salida", ['0500-0559', '0600-0659', '0700-0759', '0800-0859', '0900-0959'])

# Predicción
if st.button("¿Se va a demorar?"):
    nuevo_vuelo = pd.DataFrame({
        'MONTH': [month],
        'DAY_OF_WEEK': [day_of_week],
        'LATITUDE': [latitude],
        'LONGITUDE': [longitude],
        'PRCP': [prcp],
        'DEP_TIME_BLK': [dep_time_blk]
    })

    pred = model.predict(nuevo_vuelo)
    st.subheader("Resultado:")
    st.success("✅ No se espera demora." if pred[0] == 0 else "⚠️ Se espera una demora.")
