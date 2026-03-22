import random

class listanombres:
    """
    Clase que gestiona listas de nombres para Digipymon y entrenadores,
    permitiendo obtener nombres aleatorios.
    """

    def __init__(self, lista_nombres_digipymons, lista_nombres_entranadores):
        """
        Inicializa las listas de nombres de Digipymon y entrenadores.

        Nota:
            Aunque se reciben listas como parámetros, actualmente se sobrescriben
            con listas predefinidas dentro del constructor.

        Args:
            lista_nombres_digipymons (list): Lista de nombres de Digipymon (no utilizada actualmente).
            lista_nombres_entranadores (list): Lista de nombres de entrenadores (no utilizada actualmente).
        """
        self.lista_nombres_digipymons = [
            "PIKACHU",
            "CHARIZARD",
            "GRENINJA",
            "ESPEON",
            "SKARMORY",
            "DUNSPARCE",
            "SCYTHER",
            "DUSCLOPS",
            "MARILL",
            "BELLSPROUT",
            "MEOWTH",
            "SLAKING",
            "CLAWITZER",
            "DRUDDIGON",
            "DRAGONITE",
            "DIANCE",
            "GARDEVOIR",
            "GIBLE",
            "ZYGARDE",
            "BOLDORE",
        ]
        self.lista_nombres_entranadores = [
            "Pablo",
            "Pepe",
            "Javier",
            "Tomas",
            "Chams",
            "Jose",
            "Manuel",
            "Fernando",
            "Alejandro",
            "Jesus",
            "Guillermo",
            "Maria",
            "Sara",
            "Belen",
            "Agustina",
            "Julia",
            "Cristina",
            "Raquel",
            "Marina",
            "Lucia",
        ]

    def obtener_nombre_digipymon(self):
        """
        Devuelve un nombre aleatorio de Digipymon.

        Returns:
            str: Nombre aleatorio de la lista de Digipymon.
        """
        return random.choice(self.lista_nombres_digipymons)
    
    def obtener_nombre_entrenadores(self):
        return random.choice(self.lista_nombres_entrenadores)
