
import csv
import random
from pathlib import Path

# Dataset sintético para la actividad 4
random.seed(42)

CARPETA = Path("data")
ARCHIVO = CARPETA / "viajes_agrupamiento.csv"

CARPETA.mkdir(parents=True, exist_ok=True)

estaciones = [
    "Portal Norte",
    "Toberín",
    "Calle 100",
    "Calle 72",
    "Calle 63",
    "Universidades",
    "Museo del Oro",
    "Las Aguas"
]

registros = []

for i in range(1, 301):
    # Cantidad de tramos del viaje
    tramos = random.randint(1, 12)

    # Hora de salida en formato decimal
    hora_salida = random.choice([
        random.uniform(5, 9),    # Mañana
        random.uniform(9, 16),   # Día
        random.uniform(16, 20),  # Tarde
        random.uniform(20, 23)   # Noche
    ])

    # Supuesto: 6 minutos promedio por tramo
    # Se añade una variación simulada al tiempo
    variacion = random.uniform(-3, 8)
    tiempo_viaje = max(6, tramos * 6 + variacion)

    origen = random.choice(estaciones)
    destino = random.choice(estaciones)

    while destino == origen:
        destino = random.choice(estaciones)

    registros.append({
        "id_viaje": i,
        "origen": origen,
        "destino": destino,
        "numero_tramos": tramos,
        "hora_salida": round(hora_salida, 2),
        "tiempo_viaje_min": round(tiempo_viaje, 2)
    })

with ARCHIVO.open("w", newline="", encoding="utf-8-sig") as archivo:
    campos = [
        "id_viaje",
        "origen",
        "destino",
        "numero_tramos",
        "hora_salida",
        "tiempo_viaje_min"
    ]

    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(registros)

print(f"Dataset creado correctamente: {ARCHIVO}")
print(f"Cantidad de viajes: {len(registros)}")
print("\nPrimeros 5 registros:")

for registro in registros[:5]:
    print(registro)
