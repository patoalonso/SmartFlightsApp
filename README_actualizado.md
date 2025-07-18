
# ✈️ Smart Flights Delay Predictor

Este repositorio contiene una aplicación web desarrollada con **Streamlit** que permite predecir si un vuelo sufrirá una **demora superior a 15 minutos** en función de variables como el mes, día de la semana, ubicación del aeropuerto, precipitaciones y horario de salida.

La aplicación fue desarrollada como parte del proyecto final del curso **Data Science II** y está basada en un modelo K-Nearest Neighbors entrenado y encapsulado en un pipeline que incluye el preprocesamiento completo.

## 📦 Contenido del repositorio

- `streamlit_prediccion_vuelos.py`: código de la interfaz de usuario en Streamlit  
- `modelo_knn_pipeline.pkl`: modelo KNN entrenado con preprocesamiento incluido  
  🔗 **Descargalo desde Drive:** [modelo_knn_pipeline.pkl](https://drive.google.com/uc?export=download&id=1-WfkwXzHs1xJMZSOZM1bo5YSMe1TV5Rg)
- `requirements.txt`: dependencias necesarias para ejecutar la app

## 🚀 Cómo ejecutar la app

### 1. Clonar el repositorio y navegar al directorio

```bash
git clone https://github.com/tu_usuario/SmartFlightsApp.git
cd SmartFlightsApp
```

### 2. Ejecutar localmente (opcional)

```bash
pip install -r requirements.txt
streamlit run streamlit_prediccion_vuelos.py
```

### 3. Publicar en Streamlit Cloud

1. Subir este repositorio a GitHub.
2. Ingresar a [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Seleccionar este repositorio y el archivo `streamlit_prediccion_vuelos.py` como script principal.
4. Hacer clic en **Deploy**.

¡La aplicación estará disponible online para ser utilizada por cualquier usuario!

## 📌 Variables utilizadas por el modelo

- `MONTH`: Mes del vuelo (1 a 12)
- `DAY_OF_WEEK`: Día de la semana (1 = Lunes, 7 = Domingo)
- `LATITUDE`: Latitud del aeropuerto de salida
- `LONGITUDE`: Longitud del aeropuerto de salida
- `PRCP`: Precipitación acumulada
- `DEP_TIME_BLK`: Bloque horario del despegue (ej. '0500-0559')

---

Desarrollado por Patricia Alonso · Curso Data Science II · 2025
