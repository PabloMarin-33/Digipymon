import random
import listanombres
import digipymon
import jugador


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
    print("===Menu===")
    print("===1. Buscar Digipymon ===")
    print("===2. Luchar con Entrenador ===")
    print("===3. Ir a la Tienda ===")
    print("===4. Usar Onjetos ===")
    print("===5. Consultar Inventario ===")
    print("===6. Consultar Digipymon ===")
    print("===7. Salir ===")

    return input(("Introduce tu opción: "))


def buscar_digipymon(jugador, inventario):
    digipymon_salvaje = generar_digipymon_aleatorio()
    print(f"¡Has encontrado un {digipymon_salvaje.nombre}!")
    print(digipymon_salvaje)

    probabilidad_captura = 100 - (digipymon_salvaje.nivel * 10)
    print(f"Probabilidad de captura: {probabilidad_captura}%")

    decision = input("¿Quieres capturar el Digipymon? (s/n): ").lower()

    if decision == "s":
        if jugador.cantidad_digipymon >= 6:
            print("¡No tienes espacio para más Digipymon!")
            return
        if (
            "digipyballs" not in inventario.objetos
            or inventario.objetos["digipyballs"] <= 0
        ):
            print("¡No tienes digipyballs!")
            return

        inventario.usar_objeto("digipyballs")
        intento = random.randint(1, 100)
        if intento <= probabilidad_captura:
            jugador.añadir_digipymon(digipymon_salvaje)
            print(f"¡Has capturado a {digipymon_salvaje.nombre}!")
        else:
            print(f"¡{digipymon_salvaje.nombre} se ha escapado!")
    else:
        print("Has huido del Digipymon.")
