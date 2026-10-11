# Descripción de los datos

## 1. Objetivo

El objetivo de este proyecto es aplicar un algoritmo de aprendizaje no supervisado para identificar patrones similares entre diferentes viajes simulados del sistema de transporte de Bogotá. Para ello, se utiliza el algoritmo K-Means, que agrupa los registros según sus características.

## 2. Fuente de los datos

El conjunto de datos fue generado mediante un programa desarrollado en Python. Contiene 300 registros de viajes simulados.

**Importante:** los datos son sintéticos y no provienen de una fuente oficial de TransMilenio. Se utilizan con fines académicos para demostrar el funcionamiento del algoritmo.

## 3. Descripción de las variables

- **id_viaje:** identificador único de cada registro.
- **origen:** estación de origen simulada.
- **destino:** estación de destino simulada.
- **numero_tramos:** cantidad de tramos del viaje.
- **hora_salida:** hora de salida expresada en formato decimal.
- **tiempo_viaje_min:** duración estimada del viaje en minutos.

## 4. Preparación de los datos

Para aplicar el algoritmo se seleccionaron tres variables numéricas: `numero_tramos`, `hora_salida` y `tiempo_viaje_min`.

Posteriormente, se utilizó `StandardScaler` de la biblioteca Scikit-learn para estandarizar estas variables y evitar que sus diferentes escalas influyeran desproporcionadamente en el agrupamiento.

Las variables de origen y destino se conservaron en el conjunto de datos, pero no se utilizaron directamente para entrenar el modelo.

## 5. Generación de los datos

El programa genera viajes con entre 1 y 12 tramos. Para estimar su duración, utiliza como referencia seis minutos por tramo y agrega una variación aleatoria.

Las horas de salida se generan dentro de diferentes franjas del día, con el propósito de representar distintos horarios de desplazamiento.

## 6. Limitaciones

Los resultados dependen de las reglas y valores aleatorios utilizados para generar los datos. Por tanto, los grupos identificados representan patrones de la simulación y no necesariamente el comportamiento real de los usuarios del transporte público de Bogotá.

Para realizar un análisis real sería necesario utilizar datos confiables de viajes, horarios, estaciones y tiempos de desplazamiento.
