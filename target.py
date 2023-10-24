casos_pruebas = int(input())

for _ in range(casos_pruebas):
    puntajes = {1:0, 2:0, 3:0, 4:0, 5:0}
    posiciones = []
    for i in range(10):
        fila_i = input()
        for j in range(len(fila_i)):
            if fila_i[j] == 'X':
                posiciones.append((i,j))
    for posicion in posiciones:
        if (posicion[0] == 0 or posicion[1] == 0) or (posicion[0] == 9 or posicion[1] == 9):
            puntajes[1] += 1
        elif (posicion[0] == 1 or posicion[1] == 1) or (posicion[0] == 8 or posicion[1] == 8):
            puntajes[2] += 1
        elif (posicion[0] == 2 or posicion[1] == 2) or (posicion[0] == 7 or posicion[1] == 7):
            puntajes[3] += 1
        elif (posicion[0] == 3 or posicion[1] == 3) or (posicion[0] == 6 or posicion[1] == 6):
            puntajes[4] += 1
        else:
            puntajes[5] += 1
        resultado = 0
        for puntaje in puntajes:
            resultado = resultado + (puntaje * puntajes[puntaje])
    print(resultado)

