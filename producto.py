class Producto:
    def __init__(self, id, nombre, categoria, fecha, precio, unidades):
        self.id = int(id)
        self.nombre = nombre
        self.categoria = categoria
        self.fecha = fecha
        self.precio = float(precio)
        self.unidades = int(unidades)

    def total_venta(self):
        return self.precio * self.unidades
