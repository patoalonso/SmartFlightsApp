
# ✈️ Smart Flights Delay Predictor

Este repositorio contiene una aplicación web desarrollada con **Streamlit** que permite predecir si un vuelo sufrirá una **demora superior a 15 minutos**. Utiliza datos históricos del tráfico aéreo y un modelo de aprendizaje supervisado basado en **K-Nearest Neighbors (KNN)**.

La aplicación fue desarrollada como parte del proyecto final del curso **Data Science II**. El modelo fue encapsulado en un pipeline que incluye el preprocesamiento completo y fue serializado utilizando `cloudpickle`, lo que permite su despliegue en entornos reales.

---

## 📦 Contenido del repositorio

- `streamlit_prediccion_vuelos.py`: Interfaz web construida con Streamlit  
- `modelo_knn_pipeline.pkl`: Modelo entrenado y serializado  
- `requirements.txt`: Dependencias necesarias para ejecutar la app  

> 📥 [Descargar modelo directamente desde Google Drive](https://drive.google.com/uc?export=download&id=1-WfkwXzHs1xJMZSOZM1bo5YSMe1TV5Rg)

---

## 🎯 Objetivo del proyecto

Predecir si un vuelo partirá con una demora mayor a 15 minutos, utilizando variables simples y accesibles que el usuario puede completar fácilmente. El modelo está pensado para asistir a:

- Pasajeros frecuentes que quieren anticipar demoras  
- Aplicaciones móviles de seguimiento de vuelos  
- Aerolíneas o gestores aeroportuarios en tareas de monitoreo  

---

## 📌 Variables utilizadas en el modelo

- `CARRIER_NAME`: Nombre de la aerolínea  
- `DEPARTING_AIRPORT`: Aeropuerto de salida (código IATA)  
- `MONTH`: Mes del vuelo (1 a 12)  
- `DAY_OF_WEEK`: Día de la semana (1 = Lunes, ..., 7 = Domingo)  
- `DEP_TIME_BLK`: Bloque horario del despegue (ej. '0500-0559')  

Estas variables fueron seleccionadas por su interpretabilidad para el usuario y su relevancia predictiva.

---

## 🧠 Detalles del modelo

El modelo fue entrenado utilizando un pipeline de `scikit-learn` con:

- `OneHotEncoder` para las variables categóricas  
- `StandardScaler` para variables numéricas (aunque en este caso no fue necesario)  
- `KNeighborsClassifier` como algoritmo final de clasificación  

El pipeline completo fue entrenado en Google Colab y exportado con `cloudpickle` para facilitar su integración en la aplicación.

---

## 🚀 Cómo ejecutar la app

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/SmartFlightsApp.git
cd SmartFlightsApp
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

```bash
streamlit run streamlit_prediccion_vuelos.py
```

---

## ☁️ Cómo desplegar en Streamlit Cloud

1. Subí el repositorio a tu cuenta de GitHub  
2. Ingresá en [https://streamlit.io/cloud](https://streamlit.io/cloud)  
3. Seleccioná el repositorio y el archivo principal `streamlit_prediccion_vuelos.py`  
4. Hacé clic en **Deploy**  
5. Subí también el archivo `modelo_knn_pipeline.pkl` al mismo repositorio  

⚠️ Recordá que si usás links externos (como Drive), el archivo `.pkl` debe ser accesible y público. En esta versión usamos carga **local** para evitar bloqueos por descargas masivas.

---

## 👤 Autora

**Patricia Alonso**  
Proyecto Final · Curso Data Science II · 2025
