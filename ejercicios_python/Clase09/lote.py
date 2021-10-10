class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, cantidad):
        if self.cajones >= cantidad:
            self.cajones -= cantidad

    def __repr__(self):
        return f'Lote(\'{self.nombre}\', {self.cajones}, {self.precio})'