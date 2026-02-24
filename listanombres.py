import random

class listanombres:
    def __init__(self, lista_nombres_digipymons, lista_nombres_entranadores):
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
        return random.choice(self.lista_nombres_digipymons)
    
    def obtener_nombre_entrenadores(self):
        return random.choice(self.lista_nombres_entrenadores)
