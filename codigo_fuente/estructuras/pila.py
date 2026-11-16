class Pila:

    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # Agrega el elemento en la cima (al final de la lista)
        self.items.append(elemento)

    def desapilar(self):
        # Saca y devuelve el último elemento agregado
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0