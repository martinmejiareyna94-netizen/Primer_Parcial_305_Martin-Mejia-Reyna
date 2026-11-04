colores = ["Azul", "Morado", "Rojo", "Amarillo", "Verde"]
color = input("Ingresa el color: ")
encontrado = False
for contador in colores:
    print(contador)
    #Si el color actual es "Rojo", detener el bucle
    if contador == color:
        print("Color encontrado! Saliendo del bucle")
        encontrado = True
        break
if not encontrado:
    print("El color",color, "no se encontro")