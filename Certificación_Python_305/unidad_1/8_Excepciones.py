try:
    #Ejemplo 1 sin manejo de excepciones
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    resultado = numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("No se puede divividir entre cero")
except ValueError:
    print("Solo son numeros")