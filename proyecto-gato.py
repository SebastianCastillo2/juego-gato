import random
def crear_tablero():
    tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return tablero
def imprimir_tablero(tablero):
    fila = 0
    while fila < 3:
        print(f"{tablero[fila][0]}|{tablero[fila][1]}|{tablero[fila][2]}")
        if fila < 2:
            print("-" * 5)
        fila += 1
def movimiento_jugador(tablero, jugador):
    while True:
        fila = int(input("Elige fila (0, 1, 2): "))
        while fila >=3:
            print("movimiento invalido fuera del limite reintentalo")
            fila = int(input("Elige fila (0, 1, 2): "))
        columna = int(input("Elige columna (0, 1, 2): "))
        while columna >=3:
            print("movimiento invalido fuera del limite reintentalo")
            columna = int(input("Elige columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Casilla ocupada!")
def hay_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False
def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True
def movimiento_ia(tablero):
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = "O"
def juego_completo():
    victorias_x = 0
    victorias_y = 0
    partidas = 0
    while partidas <4:
        tablero = crear_tablero()
        jugador_actual = "X"
        while True:
            imprimir_tablero(tablero)
            print(f"Turno de {jugador_actual}")
            if jugador_actual == "X":
                movimiento_jugador(tablero, jugador_actual)
            else:
                movimiento_ia(tablero)
            if hay_ganador(tablero):
                print(f"¡{jugador_actual} ha ganado!")
                if jugador_actual == "X":
                    victorias_x += 1
                else:
                    victorias_y += 1
                partidas += 1
                break
            if tablero_lleno(tablero):
                print("¡Empate!")
                partidas += 1
                break
            if(jugador_actual=="O"):
                jugador_actual="X"
            else:
                jugador_actual = "O"
        print(f"Marcador actual: Jugador X = {victorias_x}, Jugador O = {victorias_y}")
juego_completo()