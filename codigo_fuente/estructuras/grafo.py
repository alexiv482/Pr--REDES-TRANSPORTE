class Grafo:
    def __init__(self, adyacencia=None, dirigido=False):
        self.dirigido = dirigido
        self.adyacencia = {}
        if adyacencia:
            for estacion, vecinos in adyacencia.items():
                self.adyacencia[estacion] = list(vecinos)

    def agregar_estacion(self, estacion):
        if estacion not in self.adyacencia:
            self.adyacencia[estacion] = []

    def agregar_conexion(self, origen, destino):
        self.agregar_estacion(origen)
        self.agregar_estacion(destino)
        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)
        if not self.dirigido and origen not in self.adyacencia[destino]:
            self.adyacencia[destino].append(origen)

    def obtener_vecinos(self, estacion):
        return self.adyacencia.get(estacion, [])

    def obtener_estaciones(self):
        return list(self.adyacencia.keys())

    def mostrar_red(self):
        for estacion, vecinos in self.adyacencia.items():
            print(f"  {estacion} -> {', '.join(vecinos)}")

    # Métodos de compatibilidad por si en bfs.py o dfs.py tratas el grafo como diccionario
    def __getitem__(self, estacion):
        return self.adyacencia[estacion]

    def __contains__(self, estacion):
        return estacion in self.adyacencia

    def get(self, estacion, defecto=None):
        return self.adyacencia.get(estacion, defecto)