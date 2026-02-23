class enemigo:
    def __init__(self, nombre, lista_digipymon, cantidad_digipymon):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1