from conocimiento import conexiones
from rutas import encontrar_mejor_ruta
from datetime import datetime, timedelta


def mostrar_estaciones():

    print("\nEstaciones disponibles:")

    for estacion in conexiones:
        print("-", estacion)


def main():

    print("=" * 55)
    print(" SISTEMA INTELIGENTE DE RUTAS")
    print(" Transporte Masivo")
    print("=" * 55)

    mostrar_estaciones()

    origen = input("\nIngrese la estación de origen: ")
    destino = input("Ingrese la estación de destino: ")

    # Validar origen
    if origen not in conexiones:

        print("\nLa estación de origen no existe.")
        return

    # Validar destino
    if destino not in conexiones:

        print("\nLa estación de destino no existe.")
        return

    # Buscar ruta
    ruta, tiempo_total = encontrar_mejor_ruta(
        conexiones,
        origen,
        destino
    )

    if ruta is None:

        print("\nNo existe una ruta disponible entre estas estaciones.")
        return

    # Solicitar hora de salida
    hora_salida = input(
        "\nIngrese la hora de salida (HH:MM): "
    )

    try:

        hora = datetime.strptime(
            hora_salida,
            "%H:%M"
        )

    except ValueError:

        print("\nFormato incorrecto. Utilice HH:MM.")
        return

    # Calcular hora estimada de llegada
    hora_llegada = hora + timedelta(
        minutes=tiempo_total
    )

    print("\n" + "=" * 55)
    print(" RESULTADO DE LA RUTA")
    print("=" * 55)

    print("\nOrigen:")
    print(origen)

    print("\nDestino:")
    print(destino)

    print("\nRuta recomendada:")

    for i, estacion in enumerate(ruta, start=1):

        print(f"{i}. {estacion}")

    print("\nNúmero de desplazamientos:",
          len(ruta) - 1)

    print(
        "\nTiempo estimado:",
        tiempo_total,
        "minutos"
    )

    print(
        "\nHora de salida:",
        hora.strftime("%H:%M")
    )

    print(
        "Hora estimada de llegada:",
        hora_llegada.strftime("%H:%M")
    )

    print("\n" + "=" * 55)


if __name__ == "__main__":
    main()