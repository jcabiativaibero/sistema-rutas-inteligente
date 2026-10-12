
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Rutas del proyecto
ARCHIVO_DATOS = Path("data") / "viajes_agrupamiento.csv"
CARPETA_RESULTADOS = Path("resultados") / "actividad3"
CARPETA_RESULTADOS.mkdir(parents=True, exist_ok=True)

# 1. Cargar los datos
datos = pd.read_csv(ARCHIVO_DATOS)

print("APRENDIZAJE SUPERVISADO")
print("-" * 45)
print(f"Registros cargados: {len(datos)}")

# 2. Seleccionar variables de entrada y objetivo
variables_entrada = [
    "numero_tramos",
    "hora_salida"
]
variable_objetivo = "tiempo_viaje_min"

X = datos[variables_entrada]
y = datos[variable_objetivo]

# 3. Separar datos para entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# 4. Entrenar el modelo
modelo = DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)
modelo.fit(X_train, y_train)

# 5. Realizar predicciones
predicciones = modelo.predict(X_test)

# 6. Evaluar el modelo
mae = mean_absolute_error(y_test, predicciones)

print(f"Registros de entrenamiento: {len(X_train)}")
print(f"Registros de prueba: {len(X_test)}")
print(f"Error absoluto medio (MAE): {mae:.2f} minutos")

# 7. Guardar las predicciones
resultados = X_test.copy()
resultados["tiempo_real_min"] = y_test
resultados["tiempo_predicho_min"] = predicciones
resultados["error_absoluto_min"] = abs(
    resultados["tiempo_real_min"]
    - resultados["tiempo_predicho_min"]
)

archivo_csv = CARPETA_RESULTADOS / "predicciones.csv"
resultados.to_csv(
    archivo_csv,
    index=False,
    encoding="utf-8-sig"
)

# 8. Comparar tiempos reales y predichos
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predicciones, alpha=0.7)

limite_min = min(y_test.min(), predicciones.min())
limite_max = max(y_test.max(), predicciones.max())

plt.plot(
    [limite_min, limite_max],
    [limite_min, limite_max],
    linestyle="--"
)

plt.title("Tiempos reales frente a predicciones")
plt.xlabel("Tiempo real (minutos)")
plt.ylabel("Tiempo predicho (minutos)")
plt.grid(True, alpha=0.3)
plt.tight_layout()

archivo_grafica = (
    CARPETA_RESULTADOS / "comparacion_predicciones.png"
)
plt.savefig(archivo_grafica, dpi=150)
plt.close()

print(f"Predicciones guardadas en: {archivo_csv}")
print(f"Gráfica guardada en: {archivo_grafica}")
