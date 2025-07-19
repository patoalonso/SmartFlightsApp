✈️ Smart Flights App

Esta aplicación permite predecir si un vuelo sufrirá una demora mayor a 15 minutos usando un modelo KNN entrenado con datos históricos de vuelos y condiciones de operación.

📌 Variables utilizadas en el modelo
El modelo ha sido reentrenado utilizando variables más intuitivas para el usuario final:

CARRIER_NAME: Compañía aérea (ej. American Airlines Inc.)

DEPARTING_AIRPORT: Aeropuerto de salida (JFK, LGA, EWR)

MONTH: Mes del vuelo

DAY_OF_WEEK: Día de la semana

DEP_TIME_BLK: Franja horaria de salida (ej. 0500-0559)

Estas variables se seleccionaron por su disponibilidad y utilidad práctica para una app de predicción.

🧠 Modelo y preprocesamiento
Se utilizó un pipeline de scikit-learn con:

OneHotEncoder para las variables categóricas

StandardScaler para las numéricas

KNeighborsClassifier como modelo final

El pipeline fue serializado utilizando cloudpickle.
