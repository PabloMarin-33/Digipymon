import random
import listanombres
import digipymon
import jugador
import inventario


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
    print("\n=== MENU ===")
    print("1. Buscar Digipymon")
    print("2. Luchar con Entrenador")
    print("3. Ir a la Tienda")
    print("4. Usar Objetos")
    print("5. Consultar Inventario")
    print("6. Consultar Digipymon")
    print("7. Salir")

    return input("Introduce tu opción: ")


def buscar_digipymon(jugador, inventario):

    digipymon_salvaje = generar_digipymon_aleatorio()

    print(f"\n¡Has encontrado un {digipymon_salvaje.nombre}!")
    print(digipymon_salvaje)

    probabilidad_captura = 100 - (digipymon_salvaje.nivel * 10)

    print(f"Probabilidad de captura: {probabilidad_captura}%")

    decision = input("¿Quieres capturar el Digipymon? (s/n): ").lower()

    if decision == "s":

        if jugador.cantidad_digipymon >= 6:
            print("¡No tienes espacio para más Digipymon!")
            return

        if "digipyballs" not in inventario.objetos:
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


def combate(jugador):

    nombres_manager = listanombres.listanombres([], [])

    nombre_enemigo = nombres_manager.obtener_nombre_entrenadores()

    print(f"\n¡El entrenador {nombre_enemigo} te ha desafiado!")

    equipo_enemigo = []

    for i in range(len(jugador.lista_digipymon)):
        equipo_enemigo.append(generar_digipymon_aleatorio())

    print(f"{nombre_enemigo} tiene {len(equipo_enemigo)} Digipymon preparados.")

    decision = input("¿Quieres combatir? (s/n): ").lower()

    if decision != "s":
        jugador.digicoins = max(0, jugador.digicoins - 1)
        print(f"Has huido. Pierdes 1 digicoin. Saldo: {jugador.digicoins}")
        return

    victorias = 0
    derrotas = 0

    for i in range(len(jugador.lista_digipymon)):

        mi_digi = jugador.lista_digipymon[i]
        su_digi = equipo_enemigo[i]

        print(f"\nRonda {i+1}: {mi_digi.nombre} (HP: {mi_digi.vida}, ATK: {mi_digi.ataque}) vs {su_digi.nombre} (ATK: {su_digi.ataque})")

        if mi_digi.vida <= 0:
            derrotas += 1
            print(f"{mi_digi.nombre} no puede luchar porque tiene 0 de vida.")
            continue

        if mi_digi.ataque > su_digi.ataque:

            victorias += 1
            mi_digi.vida -= su_digi.ataque

            print("¡Ganaste la ronda!")

        else:

            derrotas += 1
            diferencia = su_digi.ataque - mi_digi.ataque
            mi_digi.vida -= diferencia

            print("Perdiste la ronda.")

        if mi_digi.vida <= 0:
            mi_digi.vida = 0
            print(f"{mi_digi.nombre} se ha debilitado.")

        else:
            print(f"Vida restante de {mi_digi.nombre}: {mi_digi.vida}")

    print("\n=== RESULTADO ===")

    if victorias > derrotas:

        jugador.digicoins += victorias
        print(f"¡Victoria! Ganas {victorias} digicoins.")

    elif derrotas > victorias:

        jugador.digicoins = max(0, jugador.digicoins - derrotas)
        print(f"Derrota. Pierdes {derrotas} digicoins.")

    else:
        print("Empate.")

    print(f"Saldo final: {jugador.digicoins} Digicoins")


def digishop(jugador, inventario):

    while True:

        print("\n=== TIENDA DIGIPYMON ===")
        print(f"Tus Digicoins: {jugador.digicoins}")

        print("1. Digipyballs ---- 5 Digicoins")
        print("2. Pocion --------- 3 Digicoins (+10 Vida)")
        print("3. Baya Zidra ----- 4 Digicoins (+5 Ataque)")
        print("4. Salir")

        opcion = input("¿Qué deseas comprar? (1-4): ")

        if opcion == "4":
            break

        precios = {"1": 5, "2": 3, "3": 4}
        nombres_items = {"1": "digipyballs", "2": "pocion", "3": "baya"}

        if opcion in precios:

            coste = precios[opcion]
            item = nombres_items[opcion]

            if jugador.digicoins >= coste:

                jugador.digicoins -= coste
                inventario.añadir_objeto(item, 1)

                print(f"Has comprado {item}")

            else:

                print("No tienes suficientes Digicoins.")

        else:
            print("Opción inválida")


jugador1 = jugador.jugador("Jugador", [], 0, 10)
inventario1 = inventario.inventario()

while True:

    opcion = menu()

    if opcion == "1":
        buscar_digipymon(jugador1, inventario1)

    elif opcion == "2":
        combate(jugador1)

    elif opcion == "3":
        digishop(jugador1, inventario1)

    elif opcion == "5":
        print(inventario1.objetos)

    elif opcion == "6":
        jugador1.consultar_digipymon()

    elif opcion == "7":
        print("Saliendo del juego...")
        break

    else:
        print("Opción no válida")

def usar_item(jugador, inventario):

    if len(inventario.objetos) == 0:
        print("Tu inventario está vacío.")
        return

    print("\n=== INVENTARIO ===")

    for objeto, cantidad in inventario.objetos.items():
        print(f"{objeto}: {cantidad}")

    item = input("¿Qué objeto quieres usar?: ").lower()

    if item not in inventario.objetos:
        print("No tienes ese objeto.")
        return

    if item == "digipyballs":
        print("Las digipyballs solo se usan para capturar Digipymon.")
        return

    if len(jugador.lista_digipymon) == 0:
        print("No tienes Digipymon.")
        return

    print("\n=== TUS DIGIPYMON ===")

    for i, digi in enumerate(jugador.lista_digipymon):
        print(f"{i+1}. {digi}")

    eleccion = int(input("¿A qué Digipymon quieres usarle el objeto?: ")) - 1

    if eleccion < 0 or eleccion >= len(jugador.lista_digipymon):
        print("Selección inválida.")
        return

    digimon = jugador.lista_digipymon[eleccion]

    if item == "pocion":

        digimon.vida += 10
        print(f"{digimon.nombre} ha recuperado 10 puntos de vida.")

    elif item == "anabolizantes":

        digimon.ataque += 5
        print(f"{digimon.nombre} ha ganado 5 puntos de ataque.")

    inventario.usar_objeto(item)

    print("Objeto usado correctamente.")
