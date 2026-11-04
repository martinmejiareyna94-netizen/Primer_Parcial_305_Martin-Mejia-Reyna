promedio = [9,10,6,5,7]
#1. Encontrar el promedio mas bajo usando ciclo for
#Suponemos inicialmente que el promedio mas bajo es
promedio_bajo = promedio[0]
promedio_alto = promedio[0]
for contador in promedio:
    if contador < promedio_bajo:
        promedio_bajo = contador
    elif contador > promedio_alto:
        promedio_bajo = contador
print(promedio_bajo)
print(promedio_alto)