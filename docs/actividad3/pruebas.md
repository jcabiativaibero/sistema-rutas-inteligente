# Actividad 3: Pruebas y resultados

## 1. Objetivo de las pruebas

Verificar la carga de los datos, el entrenamiento del modelo supervisado, la generación de predicciones y la evaluación de los resultados.

## 2. Configuración

- Lenguaje: Python.
- Bibliotecas: Pandas, Scikit-learn y Matplotlib.
- Modelo: `DecisionTreeRegressor`.
- Profundidad máxima: 5.
- Registros totales: 300.
- Registros de entrenamiento: 240.
- Registros de prueba: 60.

## 3. Resultados

El programa se ejecutó correctamente y generó las predicciones para los 60 registros de prueba.

El error absoluto medio (MAE) obtenido fue de 2,44 minutos. Esta métrica representa el promedio de las diferencias absolutas entre los tiempos simulados y los tiempos predichos.

## 4. Archivos generados

- `resultados/actividad3/predicciones.csv`
- `resultados/actividad3/comparacion_predicciones.png`

## 5. Conclusión

Las pruebas muestran que el árbol de decisión pudo aprender una relación entre el número de tramos, la hora de salida y el tiempo estimado de los viajes simulados.

El MAE obtenido permite evaluar el desempeño del modelo sobre el conjunto de prueba. Sin embargo, como los datos son sintéticos, se necesitarían datos reales y una validación adicional para evaluar su utilidad en situaciones reales.
