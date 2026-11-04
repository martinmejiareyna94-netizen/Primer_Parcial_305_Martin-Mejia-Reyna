mapa = [
    [".",".",".","."],
    [".","b",".","."],
    [".",".",".","x"],
    [".",".",".","."]
]
filas = len(mapa)
columnas = len(mapa[0])
#Recorriendo la matriz con ciclos anidados
#Ciclo externo para manejar filas (i)
for i in range(filas):
    #Ciclo interno para manejar columnas (i)
    for j in range(columnas):
        #Verificanmos si encontramos el tesoro
        if mapa [i][j]=="x":
            print(f"Tesoro encontrado en la posición [{i}][{j}]")
        if mapa [i][j]=="b":
            print(f"Tesoro encontrado en la posición [{i}][{j}]")