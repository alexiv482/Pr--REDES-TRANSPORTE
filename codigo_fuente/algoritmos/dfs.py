from codigo_fuente.estructuras.pila import Pila


def buscar_dfs(estacion, origen, destino):
    piladfs = Pila()
    visitados = set()

    # Preparación: metemos la lista inicial en la pila
    piladfs.apilar([origen])

    while not piladfs.esta_vacia():
        # 1 y 2. Sacamos el último camino agregado y tomamos su última estación
        camino = piladfs.desapilar()
        estacion_actual = camino[-1]

        # 3. Si llegamos al destino, devolvemos la ruta encontrada
        if estacion_actual == destino:
            return camino

        # 4. Si no hemos pasado por aquí, exploramos sus vecinos
        if estacion_actual not in visitados:
            visitados.add(estacion_actual)
            vecinos = estacion.get(estacion_actual, [])

            for vecino in vecinos:
                nuevo_camino = camino.copy()
                nuevo_camino.append(vecino)
                piladfs.apilar(nuevo_camino)

    # Si la pila queda vacía sin éxito
    return None