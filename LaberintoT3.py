lab = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1]
]

res = [[0 for _ in range(9)] for _ in range(9)]

def imprime(mat):
    for f in mat:
        for c in f:
            print(f"{c},", end="")
        print()
    print()

def valida(fil, col) -> bool:
    if fil < 0 or fil >= len(lab) or col < 0 or col >= len(lab[0]):
        return False
    if lab[fil][col] == 0:
        return False
    if res[fil][col] == 1:
        return False
    return True

contador = 0
puntos_requeridos = 23

def labbas(lab, res, fil, col, puntos) -> bool:
    global contador

    if valida(fil, col):

        if lab[fil][col] == 3 or lab[fil][col] == 4:
            puntos += lab[fil][col]

        res[fil][col] = 1
        contador += 1
        print(f"Intento {contador} con {puntos} puntos:")
        imprime(res)

        if fil == 0 and col == 0:
            if puntos >= puntos_requeridos:
                return True
            else:
                res[fil][col] = 0
                return False

        if labbas(lab, res, fil - 1, col, puntos):
            return True
        elif labbas(lab, res, fil, col + 1, puntos):
            return True
        elif labbas(lab, res, fil + 1, col, puntos):
            return True
        elif labbas(lab, res, fil, col - 1, puntos):
            return True
        else:
            res[fil][col] = 0
            return False

    else:
        return False


#imprime(lab)
if labbas(lab, res, 8, 0, 0):
    print("SE ENCONTRÓ LA SALIDA CON 23 PUNTOS ")
    print("Camino marcado en la matriz:")
    imprime(res)
else:
    print("NO SE ENCONTRÓ UN CAMINO CON AL MENOS 23 PUNTOS.")
    print("Camino recorrido:")
    imprime(res)
