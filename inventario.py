class inventario:
    """
    Clase que representa un inventario de objetos, donde cada objeto
    tiene asociada una cantidad.
    """

    def __init__(self):
        """
        Inicializa un inventario vacío.
        """
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        """
        Añade una cantidad de un objeto al inventario. Si el objeto ya existe,
        incrementa su cantidad.

        Args:
            nombre (str): Nombre del objeto.
            cantidad (int): Cantidad a añadir del objeto.
        """
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre] = cantidad

    def usar_objeto(self, nombre):
        """
        Usa (consume) una unidad de un objeto del inventario. Si la cantidad
        llega a cero o menos, el objeto se elimina del inventario.

        Args:
            nombre (str): Nombre del objeto a usar.

        Nota:
            Si el objeto no existe en el inventario, no se realiza ninguna acción.
        """
        if nombre in self.objetos:
            self.objetos[nombre] -= 1
            if self.objetos[nombre] <= 0:
                del self.objetos[nombre]
