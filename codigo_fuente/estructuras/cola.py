class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # Agrega el elemento al final de la cola
        self.items.append(elemento)

    def desencolar(self):
        # Saca y devuelve el primer elemento de la cola
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.items) == 0