import random

def jugar_ppt_pape():
    opciones = ["piedra", "papel", "tijera"]
    puntaje_usuario = 0
    puntaje_maquina = 0

    for ronda in range(1, 4):
        print("\nRONDA", ronda)
        if ronda == 1:
            maquina = "tijera"
            usuario = input("Elige piedra, papel o tijera: ").lower()
            if usuario == "tijera":
                maquina = "piedra"
                while usuario == "tijera" and maquina == "piedra":
                    print("Empate, vuelve a tirar.")
                    usuario = input("Elige piedra, papel o tijera: ").lower()
                    maquina = random.choice(opciones)
            if usuario == maquina:
                maquina = "tijera"
            print("La máquina eligió:", maquina)
        elif ronda == 2:
            if puntaje_usuario == 1:
                maquina = "tijera"
            elif puntaje_maquina == 1:
                maquina = "piedra"
            else:
                maquina = random.choice(opciones)
            usuario = input("Elige piedra, papel o tijera: ").lower()
            if usuario == maquina:
                maquina = "tijera"
            while usuario == maquina:
                print("Empate, vuelve a tirar.")
                usuario = input("Elige piedra, papel o tijera: ").lower()
                maquina = random.choice(opciones)
            print("La máquina eligió:", maquina)
        else:
            if puntaje_usuario == 2:
                maquina = "piedra"
            elif puntaje_maquina == 2:
                maquina = "tijera"
            else:
                maquina = random.choice(opciones)
            usuario = input("Elige piedra, papel o tijera: ").lower()
            if usuario == maquina:
                maquina = "tijera"
            while usuario == maquina:
                print("Empate, vuelve a tirar.")
                usuario = input("Elige piedra, papel o tijera: ").lower()
                maquina = random.choice(opciones)
            print("La máquina eligió:", maquina)

        if usuario == maquina:
            print("Empate")
        elif (usuario == "piedra" and maquina == "tijera") or (usuario == "papel" and maquina == "piedra") or (usuario == "tijera" and maquina == "papel"):
            print("¡Ganaste esta ronda!")
            puntaje_usuario += 1
        else:
            print("¡La máquina ganó esta ronda!")
            puntaje_maquina += 1

    print("\n--- Resultado Final ---")
    print("Puntaje del usuario:", puntaje_usuario)
    print("Puntaje de la máquina:", puntaje_maquina)

    if puntaje_usuario > puntaje_maquina:
        print("¡Felicidades, has ganado el juego!")
    elif puntaje_usuario < puntaje_maquina:
        print("¡La máquina ha ganado el juego!")
    else:
        print("El juego terminó en empate.")
def jugar_ppt_cupe():
    opciones = ["piedra", "papel", "tijera"]
    puntaje_usuario = 0
    puntaje_maquina = 0

    for ronda in range(1, 4):
        print("\nRONDA", ronda)
        if ronda == 1:
            maquina = "piedra"
            usuario = input("Elige piedra, papel o tijera: ").lower()
            if usuario == "piedra":
                maquina = "tijera"
                while usuario == "piedra" and maquina == "tijera":
                    print("Empate, vuelve a tirar.")
                    usuario = input("Elige piedra, papel o tijera: ").lower()
                    maquina = random.choice(["piedra", "tijera"])
            if usuario == maquina:
                maquina = "piedra"
            print("La máquina eligió:", maquina)
        elif ronda == 2:
            if puntaje_usuario == 1:
                maquina = "tijera"
            elif puntaje_maquina == 1:
                maquina = "tijera"
            else:
                maquina = random.choice(opciones)
            usuario = input("Elige piedra, papel o tijera: ").lower()
            if usuario == maquina:
                maquina = "tijera"
            while usuario == maquina:
                print("Empate, vuelve a tirar.")
                usuario = input("Elige piedra, papel o tijera: ").lower()
                maquina = random.choice(["piedra", "tijera"])
            print("La máquina eligió:", maquina)
        else:
            if puntaje_usuario == 2:
                maquina = "piedra"
            elif puntaje_maquina == 2:
                maquina = "tijera"
            else:
                maquina = random.choice(opciones)
            usuario = input("Elige piedra, papel o tijera: ").lower()
            if usuario == maquina:
                maquina = "tijera"
            while usuario == maquina:
                print("Empate, vuelve a tirar.")
                usuario = input("Elige piedra, papel o tijera: ").lower()
                maquina = random.choice(["piedra", "tijera"])
            print("La máquina eligió:", maquina)

        if usuario == maquina:
            print("Empate")
        elif (usuario == "piedra" and maquina == "tijera") or (usuario == "papel" and maquina == "piedra") or (usuario == "tijera" and maquina == "papel"):
            print("¡Ganaste esta ronda!")
            puntaje_usuario += 1
        else:
            print("¡La máquina ganó esta ronda!")
            puntaje_maquina += 1

    print("\n--- Resultado Final ---")
    print("Puntaje del usuario:", puntaje_usuario)
    print("Puntaje de la máquina:", puntaje_maquina)

    if puntaje_usuario > puntaje_maquina:
        print("¡Felicidades, has ganado el juego!")
    elif puntaje_usuario < puntaje_maquina:
        print("¡La máquina ha ganado el juego!")
    else:
        print("El juego terminó en empate.")




def PPT():
    print("Quien juega?")
    print("1. PAPE")
    print("2. CUPE")
    opcion = input("Ingresa el número de la configuración deseada: ")

    if opcion == "1":
        jugar_ppt_pape()
    elif opcion == "2":
         jugar_ppt_cupe()
    else:
        print("Opción inválida. Por favor, ingresa un número válido.")
       