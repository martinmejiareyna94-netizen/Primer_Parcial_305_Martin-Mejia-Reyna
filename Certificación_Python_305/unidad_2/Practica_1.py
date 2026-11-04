nombres = []
calificacion = []
alumno = int(input("¿Cuantos alumnos quiere ingresar? "))
for contador in range(alumno):
    alumnos = input(f"Ingrese el nombre de los alumnos: {contador + 1 }: ")
    nombres.append(alumnos)
    
for contador in range(alumno):
    promedios = float(input(f"Ingrese el promedio {contador + 1}: "))
    calificacion.append(promedios)
    

promedio_alto = calificacion[1]
promedio_bajo = calificacion[0]
for contador in calificacion:
    if contador < promedio_bajo:
        promedio_bajo = contador
    elif contador > promedio_alto:
        promedio_bajo = contador
print(promedio_bajo)
print(promedio_alto)
print(nombres + calificacion)
