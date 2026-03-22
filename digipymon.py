class digipymon:
    """
    Clase que representa una criatura Digipymon con atributos básicos
    como nombre, vida, ataque, tipo y nivel.
    """

    def __init__(self, nombre, vida, ataque, tipo, nivel):
        """
        Inicializa una nueva instancia de Digipymon.

        Args:
            nombre (str): Nombre del Digipymon.
            vida (int): Cantidad de puntos de vida.
            ataque (int): Valor de ataque del Digipymon.
            tipo (str): Tipo o elemento del Digipymon.
            nivel (int): Nivel del Digipymon.
        """
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        """
        Devuelve una representación en texto del Digipymon.

        Returns:
            str: Cadena con los atributos del Digipymon.
        """
        return f"Nombre: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}, Tipo: {self.tipo}, Nivel: {self.nivel}"
