try: 
    #Declarando una lista
    materias = ["Programacion","Filosofia","Matematicas","Ingles"]
    print(materias[0])
    materias.append("Lengua y comunicacion")
    print(materias)
    materias[1] = "Biologia"
    print(materias)
    materias.remove("Matematicas")
    print(materias)
except IndexError:
    print("Indice incorrecto")