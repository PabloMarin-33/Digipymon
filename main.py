import random
import listanombres
import digipymon


def generar_digipymon_aleatorio():
    tipos = ["agua", "fuego", "planta"]
    nombres = listanombres.listanombres([], [])

    vida = random.randint(10, 20)
    ataque = random.randint(1, 10)
    nivel = random.randint(1, 3)
    tipo = random.choice(tipos)
    nombre = nombres.obtener_nombre_digipymon()

    return digipymon.digipymon(nombre, vida, ataque, tipo, nivel)

def menu():
    