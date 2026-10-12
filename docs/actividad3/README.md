# Actividad 3: Aprendizaje supervisado

## Descripción

Esta actividad implementa un modelo de aprendizaje supervisado mediante un árbol de decisión para estimar el tiempo de viaje de registros de transporte simulados.

El modelo utiliza las variables `numero_tramos` y `hora_salida` para predecir `tiempo_viaje_min`.

## Tecnologías

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Ejecución

Desde la raíz del repositorio, con el entorno virtual activado:

```powershell
python supervisado.py
```

## Resultados

Se procesaron 300 registros: 240 para entrenamiento y 60 para prueba.

El error absoluto medio (MAE) fue de 2,44 minutos.

Los resultados se guardan en `resultados/actividad3/`, junto con una gráfica que compara los tiempos observados con las predicciones del modelo.

## Limitaciones

Los datos son sintéticos y se utilizan exclusivamente con fines académicos. El resultado no representa una validación de predicciones para el sistema real de transporte de Bogotá.

## Enlaces de entrega

- Repositorio: https://github.com/jcabiativaibero/sistema-rutas-inteligente
- Video: [Agregar enlace al video de la Actividad 3]
