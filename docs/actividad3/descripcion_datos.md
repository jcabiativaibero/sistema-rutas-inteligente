# Actividad 3: Descripción de los datos

## 1. Objetivo

Aplicar un modelo de aprendizaje supervisado mediante un árbol de decisión para estimar el tiempo de viaje a partir de características de desplazamientos simulados.

## 2. Fuente de los datos

Se utilizó el archivo `data/viajes_agrupamiento.csv`, generado mediante un programa de Python para fines académicos. El conjunto contiene 300 registros simulados.

Los datos no corresponden a registros oficiales de TransMilenio ni representan mediciones reales de movilidad.

## 3. Variables utilizadas

- `numero_tramos`: número de tramos del viaje.
- `hora_salida`: hora de salida expresada en formato decimal.
- `tiempo_viaje_min`: tiempo estimado del viaje en minutos; esta es la variable objetivo que el modelo aprende a predecir.

## 4. Preparación de los datos

Se seleccionaron las variables `numero_tramos` y `hora_salida` como entradas del modelo. La variable `tiempo_viaje_min` se utilizó como objetivo.

Los datos se dividieron en dos conjuntos: 80 % para entrenamiento y 20 % para prueba. La división se realizó con `train_test_split` y `random_state=42` para facilitar la reproducibilidad.

## 5. Limitaciones

La calidad de las predicciones depende de las reglas utilizadas para generar los datos. El modelo permite demostrar el proceso de aprendizaje supervisado, pero su resultado no debe interpretarse como una estimación validada de tiempos reales de transporte.
