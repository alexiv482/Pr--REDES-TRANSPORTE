def buscar_bfs(estacion, origen, destino):
    frontera = [[origen]]
    visitados = set()

    while frontera:
        camino = frontera.pop(0)
        estacion_actual = camino[-1]

        if estacion_actual == destino:
            return camino

        if estacion_actual not in visitados:
            visitados.add(estacion_actual)
            vecinos = estacion.get(estacion_actual, [])

            for vecino in vecinos:
                nuevo_camino = camino.copy()
                nuevo_camino.append(vecino)
                frontera.append(nuevo_camino)

    return None