try:
    numero1 = float(input("Ingresa el primer numero: "))
    numero2 = float(input("Ingresa el segundo numero: "))
    resultado = numero1/numero2
except ValueError:
    print("Solo introduce numeros")
except ZeroDivisionError:
    print("Divicion entre cero")
else:
    print("El resultado es: ", resultado)
finally:
    print("Programa finalizado")