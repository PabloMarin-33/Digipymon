class jugador:
    def __init__(self, nombre, lista_digipymon, cantidad_digipymon, digicoins):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1

    def consultar_digipymon(self):
        for digipymon in self.lista_digipymon:
            print(digipymon)

    def consultar_digicoins(self):
            print("Monedero: " + self.digicoins)
