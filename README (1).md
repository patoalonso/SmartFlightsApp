# ✈️ Predicción de Demoras de Vuelo con KNN y Streamlit

Este proyecto consiste en una aplicación web interactiva desarrollada con **Streamlit** que permite predecir si un vuelo en EE. UU. sufrirá una **demora mayor a 15 minutos**. Utiliza un modelo de **K-Nearest Neighbors (KNN)** entrenado con variables operativas y meteorológicas de vuelos históricos.

## 📌 Variables utilizadas en el modelo

Para una mejor experiencia de usuario en la app, se seleccionaron variables **intuitivas** y fácilmente ingresables:

- `CARRIER_NAME`: Compañía aérea (por ejemplo: *Delta*, *American Airlines*).
- `DEPARTING_AIRPORT`: Aeropuerto de salida (por ejemplo: *JFK*, *LGA*, *EWR*).
- `MONTH`: Mes del vuelo (1 a 12).
- `DAY_OF_WEEK`: Día de la semana (1=Lunes a 7=Domingo).
- `DEP_TIME_BLK`: Bloque horario de salida (por ejemplo: *0500-0559*, *0600-0659*).

> Estas variables reemplazan a otras menos comprensibles como latitud/longitud o precipitación.

---

## 🧠 Modelo de Machine Learning

El modelo implementado es un **Pipeline de Scikit-Learn** compuesto por:

1. **Preprocesamiento**:
   - OneHotEncoder para variables categóricas (`CARRIER_NAME`, `DEPARTING_AIRPORT`, `DEP_TIME_BLK`)
   - StandardScaler para variables numéricas (`MONTH`, `DAY_OF_WEEK`)

2. **Algoritmo**: KNeighborsClassifier con `n_neighbors=5`.

3. **Exportación**: El pipeline fue serializado con `cloudpickle` y guardado como `modelo_knn_pipeline.pkl`.

---

## 🚀 Cómo ejecutar la app

1. Clonar este repositorio:

```bash
git clone https://github.com/patoalonso/SmartFlightsApp.git
cd SmartFlightsApp
```

2. Asegurarse de tener Streamlit y las dependencias necesarias:

```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:

```bash
streamlit run streamlit_prediccion_vuelos.py
```

---

## 🧪 Ejemplo de predicción

La aplicación permite cargar los datos desde un formulario visual:

- Seleccionar la aerolínea
- Elegir aeropuerto de salida
- Ingresar mes y día
- Elegir el rango horario

Y obtendrás como resultado una predicción:

```
✅ No se espera demora.
⚠️ Se espera una demora.
```

---

## 📁 Estructura del repositorio

```
SmartFlightsApp/
├── streamlit_prediccion_vuelos.py     # Script principal de la app
├── modelo_knn_pipeline.pkl            # Modelo entrenado serializado
├── requirements.txt                   # Dependencias necesarias
└── README.md                          # Este archivo
```

---

## 🌐 Visualización de la app (Streamlit Cloud)

Podés ver la app funcionando desde Streamlit Cloud en:

👉 [https://smartflightsapp.streamlit.app](https://smartflightsapp.streamlit.app) *(Reemplazar con el link de despliegue si cambió)*

---

## 📚 Dataset utilizado

El modelo fue entrenado con un subconjunto del dataset de vuelos domésticos en EE. UU. disponible en [Kaggle](https://www.kaggle.com/datasets), con foco en el análisis de la variable `DEP_DEL15`.

---

## ✍️ Autora

**Patricia Alonso** – Proyecto final para el curso **Data Science II** – 2025.
