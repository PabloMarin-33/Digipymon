class jugador:
    """
    Clase que representa a un jugador que posee una colección de Digipymon
    y una cantidad de monedas (digicoins).
    """

    def __init__(self, nombre, lista_digipymon, cantidad_digipymon, digicoins):
        """
        Inicializa una nueva instancia de jugador.

        Nota:
            Aunque se reciben `lista_digipymon`, `cantidad_digipymon` y `digicoins`,
            actualmente se inicializan con valores por defecto dentro del constructor.

        Args:
            nombre (str): Nombre del jugador.
            lista_digipymon (list): Lista inicial de Digipymon (no utilizada actualmente).
            cantidad_digipymon (int): Cantidad inicial de Digipymon (no utilizada actualmente).
            digicoins (int): Cantidad inicial de monedas (no utilizada actualmente).
        """
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    def añadir_digipymon(self, digipymon):
        """
        Añade un Digipymon a la colección del jugador y actualiza la cantidad.

        Args:
            digipymon (digipymon): Objeto de tipo Digipymon que se añadirá al jugador.
        """
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1

    def consultar_digipymon(self):
        """
        Muestra por pantalla todos los Digipymon del jugador.
        """
        for digipymon in self.lista_digipymon:
            print(digipymon)

    def consultar_digicoins(self):
        """
        Muestra por pantalla la cantidad de digicoins del jugador.
        """
        print("Monedero: " + self.digicoins)
