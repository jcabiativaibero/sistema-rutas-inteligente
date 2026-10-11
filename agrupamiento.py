
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Rutas de los archivos
ARCHIVO_DATOS = Path("data") / "viajes_agrupamiento.csv"
CARPETA_RESULTADOS = Path("resultados")

CARPETA_RESULTADOS.mkdir(parents=True, exist_ok=True)

# 1. Cargar el dataset
datos = pd.read_csv(ARCHIVO_DATOS)

print("DATASET CARGADO")
print("-" * 50)
print(f"Cantidad de viajes: {len(datos)}")
print(datos.head())

# 2. Seleccionar las variables numéricas para agrupar
variables = [
    "numero_tramos",
    "hora_salida",
    "tiempo_viaje_min"
]

X = datos[variables]

# 3. Estandarizar las variables
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)

# 4. Entrenar K-Means con tres grupos
modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

datos["grupo"] = modelo.fit_predict(X_escalado)

# 5. Evaluar la separación de los grupos
puntuacion = silhouette_score(X_escalado, datos["grupo"])

print("\nRESULTADOS DEL AGRUPAMIENTO")
print("-" * 50)
print(f"Número de grupos encontrados: {datos['grupo'].nunique()}")
print(f"Coeficiente Silhouette: {puntuacion:.3f}")

# 6. Describir las características de cada grupo
resumen = datos.groupby("grupo")[variables].mean().round(2)

print("\nPROMEDIOS POR GRUPO")
print(resumen)

# 7. Guardar los resultados
archivo_resultados = CARPETA_RESULTADOS / "viajes_agrupados.csv"
datos.to_csv(archivo_resultados, index=False, encoding="utf-8-sig")

archivo_resumen = CARPETA_RESULTADOS / "resumen_grupos.csv"
resumen.to_csv(archivo_resumen, encoding="utf-8-sig")

print(f"\nResultados guardados en: {archivo_resultados}")
print(f"Resumen guardado en: {archivo_resumen}")

# 8. Crear una gráfica de los grupos
plt.figure(figsize=(10, 6))

for grupo in sorted(datos["grupo"].unique()):
    seleccion = datos[datos["grupo"] == grupo]

    plt.scatter(
        seleccion["numero_tramos"],
        seleccion["tiempo_viaje_min"],
        label=f"Grupo {grupo}",
        alpha=0.7
    )

plt.title("Agrupamiento de viajes mediante K-Means")
plt.xlabel("Número de tramos")
plt.ylabel("Tiempo de viaje (minutos)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

archivo_grafica = CARPETA_RESULTADOS / "agrupamiento_viajes.png"
plt.savefig(archivo_grafica, dpi=150)
plt.show()

print(f"Gráfica guardada en: {archivo_grafica}")
