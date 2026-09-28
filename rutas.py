from collections import deque


TIEMPO_POR_ESTACION = 6


def encontrar_mejor_ruta(conexiones, origen, destino):

    cola = deque([origen])

    anteriores = {
        origen: None
    }

    while cola:

        estacion_actual = cola.popleft()

        if estacion_actual == destino:
            break

        for vecino in conexiones.get(estacion_actual, []):

            if vecino not in anteriores:

                anteriores[vecino] = estacion_actual
                cola.append(vecino)

    # No existe una ruta
    if destino not in anteriores:
        return None, None

    # Reconstruir la ruta
    ruta = []
    estacion = destino

    while estacion is not None:

        ruta.append(estacion)
        estacion = anteriores[estacion]

    ruta.reverse()

    # Cada desplazamiento entre estaciones
    # tiene una duración promedio de 6 minutos
    cantidad_tramos = len(ruta) - 1

    tiempo_total = cantidad_tramos * TIEMPO_POR_ESTACION

    return ruta, tiempo_total