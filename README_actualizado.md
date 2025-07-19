# ✈️ Smart Flights Delay Predictor

Este repositorio contiene una aplicación web desarrollada con **Streamlit** que permite predecir si un vuelo sufrirá una **demora superior a 15 minutos**. Utiliza datos históricos del tráfico aéreo y un modelo de aprendizaje supervisado basado en **K-Nearest Neighbors (KNN)**.

La aplicación fue desarrollada como parte del proyecto final del curso **Data Science II**. El modelo fue encapsulado en un pipeline que incluye el preprocesamiento completo y serializado con `cloudpickle` para facilitar su despliegue en entornos reales.

---

## 📦 Contenido del repositorio

- `streamlit_prediccion_vuelos.py`: interfaz web desarrollada con Streamlit  
- `modelo_knn_pipeline.pkl`: modelo KNN con preprocesamiento incluido  
- `requirements.txt`: dependencias necesarias para ejecutar la app  

> 🎯 **Accedé directamente al modelo:** [modelo_knn_pipeline.pkl](https://drive.google.com/uc?export=download&id=1-WfkwXzHs1xJMZSOZM1bo5YSMe1TV5Rg)

---

## 🎯 Objetivo del proyecto

Predecir si un vuelo partirá con una demora mayor a 15 minutos, utilizando variables simples que los usuarios pueden ingresar fácilmente, como la aerolínea, el aeropuerto y la franja horaria de salida. El resultado busca asistir tanto a **pasajeros**, como a **gestores aeroportuarios** o **aplicaciones móviles de seguimiento de vuelos**.

---

## 📌 Variables utilizadas por el modelo

- `CARRIER_NAME`: Nombre de la compañía aérea  
- `DEPARTING_AIRPORT`: Aeropuerto de salida (código IATA)  
- `MONTH`: Mes del vuelo (1 a 12)  
- `DAY_OF_WEEK`: Día de la semana (1 = Lunes, 7 = Domingo)  
- `DEP_TIME_BLK`: Bloque horario del despegue (ej. '0500-0559')  

Estas variables fueron seleccionadas por ser fácilmente interpretables por los usuarios y por su capacidad predictiva según el análisis exploratorio previo.

---

## 🚀 Cómo ejecutar la app

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/SmartFlightsApp.git
cd SmartFlightsApp

