# Pruebas y resultados del modelo

## 1. Objetivo de las pruebas

Comprobar que el programa carga los datos correctamente, ejecuta el algoritmo K-Means, asigna los viajes a grupos y genera los archivos de resultados.

## 2. Entorno de ejecución

- Lenguaje: Python.
- Procesamiento de datos: Pandas.
- Aprendizaje automático: Scikit-learn.
- Visualización: Matplotlib.
- Algoritmo: K-Means.
- Número de grupos configurado: 3.
- Cantidad de registros: 300.

## 3. Pruebas realizadas

### Prueba 1. Carga del conjunto de datos

**Resultado esperado:** cargar el archivo CSV y mostrar los registros.

**Resultado obtenido:** el programa cargó correctamente 300 viajes desde `data/viajes_agrupamiento.csv`.

**Estado:** aprobada.

### Prueba 2. Ejecución del algoritmo

**Resultado esperado:** asignar cada viaje a uno de los tres grupos.

**Resultado obtenido:** el algoritmo identificó tres grupos y asignó una etiqueta a cada registro.

**Estado:** aprobada.

### Prueba 3. Evaluación del agrupamiento

**Resultado esperado:** calcular el coeficiente Silhouette para evaluar la separación de los grupos.

**Resultado obtenido:** se obtuvo un coeficiente de 0,426, lo que sugiere una separación moderada entre los grupos.

**Estado:** aprobada.

### Prueba 4. Análisis de los grupos

Los promedios obtenidos fueron:

| Grupo | Número de tramos | Hora de salida | Tiempo de viaje (min) |
|---|---:|---:|---:|
| 0 | 8,73 | 19,04 | 54,84 |
| 1 | 3,05 | 14,85 | 20,69 |
| 2 | 9,37 | 8,14 | 58,32 |

Los resultados permiten observar un grupo de viajes relativamente cortos y dos grupos de viajes más largos, diferenciados parcialmente por la hora de salida.

**Estado:** aprobada.

### Prueba 5. Generación de archivos

**Resultado esperado:** guardar los viajes agrupados, el resumen de los grupos y la gráfica.

**Resultado obtenido:** se generaron los archivos `viajes_agrupados.csv`, `resumen_grupos.csv` y `agrupamiento_viajes.png` en la carpeta `resultados`.

**Estado:** aprobada.

## 4. Conclusión

Las pruebas confirman que el programa ejecuta correctamente el proceso de agrupamiento no supervisado sobre los datos simulados. El algoritmo K-Means permite identificar patrones según el número de tramos, la hora de salida y el tiempo estimado del viaje.

Los resultados son demostrativos y no deben interpretarse como estadísticas oficiales del sistema de transporte de Bogotá.
