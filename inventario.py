class inventario:
    def __init__(self):
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre] = cantidad
