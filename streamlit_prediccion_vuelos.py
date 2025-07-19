import streamlit as st
import pandas as pd
import cloudpickle

# Cargar modelo local
with open("modelo_knn_pipeline.pkl", "rb") as f:
    model = cloudpickle.load(f)

# Configuración de la app
st.set_page_config(page_title="¿Se va a demorar mi vuelo?", layout="centered")
st.title("✈️ Predicción de Demoras de Vuelo con KNN")
st.markdown("Complete los datos del vuelo para saber si tendrá una demora mayor a 15 minutos.")

# Formulario
carrier = st.selectbox("Compañía aérea", ['American Airlines Inc.', 'United Air Lines Inc.', 'Delta Air Lines Inc.'])  # Podés ajustar valores
airport = st.selectbox("Aeropuerto de salida", ['JFK', 'LGA', 'EWR'])  # Podés ajustar valores
month = st.selectbox("Mes", list(range(1, 13)))
day_of_week = st.selectbox("Día de la semana", [1, 2, 3, 4, 5, 6, 7], format_func=lambda x: ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"][x-1])
dep_time_blk = st.selectbox("Bloque horario de salida", ['0500-0559', '0600-0659', '0700-0759', '0800-0859', '0900-0959'])

# Predicción
if st.button("¿Se va a demorar?"):
    nuevo_vuelo = pd.DataFrame({
        'CARRIER_NAME': [carrier],
        'DEPARTING_AIRPORT': [airport],
        'MONTH': [month],
        'DAY_OF_WEEK': [day_of_week],
        'DEP_TIME_BLK': [dep_time_blk]
    })

    pred = model.predict(nuevo_vuelo)
    st.subheader("Resultado:")
    st.success("✅ No se espera demora." if pred[0] == 0 else "⚠️ Se espera una demora.")
