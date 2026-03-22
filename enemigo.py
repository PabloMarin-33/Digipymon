class enemigo:
    """
    Clase que representa a un enemigo que posee una colección de Digipymon.
    """

    def __init__(self, nombre, lista_digipymon, cantidad_digipymon):
        """
        Inicializa una nueva instancia de enemigo.

        Nota:
            Aunque se reciben `lista_digipymon` y `cantidad_digipymon` como parámetros,
            actualmente se inicializan como valores vacíos o cero dentro del constructor.

        Args:
            nombre (str): Nombre del enemigo.
            lista_digipymon (list): Lista inicial de Digipymon (no utilizada actualmente).
            cantidad_digipymon (int): Cantidad inicial de Digipymon (no utilizada actualmente).
        """
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    def añadir_digipymon(self, digipymon):
        """
        Añade un Digipymon a la lista del enemigo y actualiza la cantidad.

        Args:
            digipymon (digipymon): Objeto de tipo Digipymon que se añadirá al enemigo.
        """
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1
