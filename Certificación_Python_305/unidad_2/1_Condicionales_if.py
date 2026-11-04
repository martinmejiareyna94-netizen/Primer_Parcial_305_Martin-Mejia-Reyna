edad = int(input("Introduce tu edad: "))
if edad >=0 and edad <= 3 :
    print("Eres bebe")
elif edad >= 4 and edad <= 11 :
    print("Eres un niño")
elif edad >= 12 and edad <= 18 :
    print("Eres un adolecente")
elif edad >= 18 and edad <= 29:
    print("Eres un joven")
elif edad >= 30 and edad <= 40 :
    print("Eres un chavo-ruco")
elif edad >= 41 and edad <= 100:
    print("Eres un adulto")
else:
    print("Estas robando oxigeno")