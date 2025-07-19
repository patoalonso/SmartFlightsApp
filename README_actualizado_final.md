
# ✈️ Smart Flights: Predicción de Demoras Aéreas

Este proyecto utiliza técnicas de Machine Learning para predecir si un vuelo tendrá una demora mayor a 15 minutos. Se basa en datos de vuelos y condiciones del servicio aéreo en EE. UU., y culmina en una app interactiva desarrollada con Streamlit.

---

## 🎯 Objetivo

Construir un modelo de clasificación supervisada que permita predecir demoras significativas en vuelos, utilizando variables como aerolínea, aeropuerto de salida, día de la semana, mes y horario de salida.

---

## 📦 Tecnologías utilizadas

- Python (Pandas, Scikit-learn, Cloudpickle)
- Streamlit
- Google Drive (para alojar el modelo)
- Google Colab
- GitHub

---

## 📁 Estructura del repositorio

```
├── SMART_FLIGHTS_II_Alonso_Castillo.ipynb    # Notebook principal con análisis, modelado y entrenamiento
├── streamlit_prediccion_vuelos.py            # Script de la app Streamlit
├── requirements.txt                          # Dependencias del proyecto
```

🔗 El modelo `modelo_knn_pipeline.pkl` es muy pesado (4.5 GB), por lo que está alojado externamente en Google Drive:  
👉 [Descargar modelo desde Drive](https://drive.google.com/uc?id=1-WfkwXzHs1xJMZSOZM1bo5YSMe1TV5Rg)

---

## 🧠 Variables seleccionadas para la predicción

- `CARRIER_NAME`: Compañía aérea
- `DEPARTING_AIRPORT`: Aeropuerto de salida
- `MONTH`: Mes
- `DAY_OF_WEEK`: Día de la semana
- `DEP_TIME_BLK`: Franja horaria de salida

---

## 🚀 Cómo ejecutar la app

1. Cloná este repositorio o descargalo como ZIP
2. Instalá las dependencias:

```
pip install -r requirements.txt
```

3. 🔽 **Descargá el modelo `.pkl`** desde [este enlace](https://drive.google.com/uc?id=1-WfkwXzHs1xJMZSOZM1bo5YSMe1TV5Rg)
4. Guardá el archivo `modelo_knn_pipeline.pkl` en la misma carpeta del script `streamlit_prediccion_vuelos.py`
5. Ejecutá la app con:

```
streamlit run streamlit_prediccion_vuelos.py
```

---

## 🖥️ Captura de la interfaz

La app permite seleccionar los valores del vuelo a evaluar y obtener una predicción clara e inmediata:

> “✅ No se espera demora.” o “⚠️ Se espera una demora.”

---

## 👩‍💻 Autor

**Patricia Alonso**  
Proyecto final - DATA SCIENCE II  
Universidad Nacional de las Artes – 2025
