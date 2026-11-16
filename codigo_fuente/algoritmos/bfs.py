from codigo_fuente.estructuras.cola import Cola


def buscar_bfs(estacion, origen, destino):
    colabfs = Cola()
    visitados = set()

    colabfs.encolar([origen])

    while not colabfs.esta_vacia():
        camino = colabfs.desencolar()
        estacion_actual = camino[-1]

        if estacion_actual == destino:
            return camino

        if estacion_actual not in visitados:
            visitados.add(estacion_actual)
            vecinos = estacion.get(estacion_actual, [])

            for vecino in vecinos:
                nuevo_camino = camino.copy()
                nuevo_camino.append(vecino)
                colabfs.encolar(nuevo_camino)

    return None