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

def combate(jugador):
    nombres_manager = listanombres.listanombres([], [])
    nombre_enemigo = nombres_manager.obtener_nombre_entrenador() 
    
    print(f"\n¡El entrenador {nombre_enemigo} te ha desafiado!")
    
    equipo_enemigo = []
    
    for i in range(len(jugador_instancia.equipo)):
        equipo_enemigo.append(generar_digipymon_aleatorio())

    print(f"{nombre_enemigo} tiene {len(equipo_enemigo)} Digipymon preparados.")

    decision = input("¿Quieres combatir? (s/n): ").lower()

    if decision != "s":
        jugador_instancia.digicoins = max(0, jugador_instancia.digicoins - 1)
        print(f"Has huido. Pierdes 1 digicoin. Saldo: {jugador_instancia.digicoins}")
        return

    victorias = 0
    derrotas = 0

    for i in range(len(jugador_instancia.equipo)):
        mi_digi = jugador_instancia.equipo[i]
        su_digi = equipo_enemigo[i]

        print(f"\nRonda {i+1}: {mi_digi.nombre} (HP: {mi_digi.vida}, ATK: {mi_digi.ataque}) vs {su_digi.nombre} (ATK: {su_digi.ataque})")

        if mi_digi.vida <= 0:
            derrotas += 1
            print(f"¡{mi_digi.nombre} no puede luchar porque tiene 0 de vida! Pierdes esta ronda.")
            continue

        if mi_digi.ataque > su_digi.ataque:
            victorias += 1
            mi_digi.vida -= su_digi.ataque
            print(f"¡Ganaste la ronda! {mi_digi.nombre} tiene más ataque.")
        else:
            derrotas += 1
            diferencia = su_digi.ataque - mi_digi.ataque
            mi_digi.vida -= diferencia
            print(f"Perdiste la ronda. {su_digi.nombre} fue superior.")

        if mi_digi.vida <= 0:
            mi_digi.vida = 0
            print(f"¡Atención! La vida de {mi_digi.nombre} ha caído a 0.")
        else:
            print(f"Vida restante de {mi_digi.nombre}: {mi_digi.vida}")

    print("\n=== RESULTADO DE LA BATALLA ===")
    if victorias > derrotas:
        jugador_instancia.digicoins += victorias
        print(f"¡Victoria total! Ganas {victorias} digicoins.")
    elif derrotas > victorias:
        jugador_instancia.digicoins = max(0, jugador_instancia.digicoins - derrotas)
        print(f"Derrota total. Pierdes {derrotas} digicoins.")
    else:
        print("Empate técnico. No hay cambio en tus digicoins.")
    
        print(f"Saldo final de Digicoins: {jugador_instancia.digicoins}")

def digishop(jugador, inventario):
    while True:
        print("\n" + "="*20)
        print("   BIENVENIDO AL CENTRO DIGIPYMON")
        print("="*20)
        print(f"Tus Digicoins: {jugador_instancia.digicoins}")
        print("-" * 20)
        print("1. Digipyballs ---- 5 Digicoins")
        print("2. Pocion --------- 3 Digicoins (+10 Vida)")
        print("3. Baya Zidra -- 4 Digicoins (+5 Ataque)")
        print("4. Salir de la tienda")
        print("-" * 20)
        
        opcion = input("¿Qué deseas comprar? (1-4): ")

        if opcion == "4":
            print("¡Gracias por su visita!")
            break

        precios = {"1": 5, "2": 3, "3": 4}
        nombres_items = {"1": "digipyballs", "2": "pocion", "3": "Baya Zidra"}

        if opcion in precios:
            coste = precios[opcion]
            item_nombre = nombres_items[opcion]

            if jugador.digicoins >= coste:
                jugador.digicoins -= coste
                
                if item_nombre in inventario_instancia.objetos:
                    inventario_instancia.objetos[item_nombre] += 1
                else:
                    inventario_instancia.objetos[item_nombre] = 1
                
                print(f"¡Compra exitosa! Has adquirido {item_nombre}.")
                print(f"Saldo restante: {jugador_instancia.digicoins} Digicoins.")
            else:
                print(f"No tienes suficientes Digicoins. Te faltan {coste - jugador_instancia.digicoins}.")
        else:
            print("Opción no válida, intenta de nuevo.")
