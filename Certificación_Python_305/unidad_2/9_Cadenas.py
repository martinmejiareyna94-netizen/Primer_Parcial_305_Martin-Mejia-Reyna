#Cadenas y concatrenacion con (+)
cadena1 = 'Hola '
cadena2 = "Mundo "
multilinea = """Esto es un cadena 
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#Cadenas y repiticion
eco = "ja"*5
print(eco)
#Cambiar una cadena de minuscula a mayuscula
tu_nombre = 'Martin'
print(tu_nombre.upper())
#Cambiar una cadena de mayusculas a minusculas
print(tu_nombre.lower())
#Remplazar texto en una cadena
frase = "Me gusta programcion"
print(frase.replace("Programacion","Historia"))
#Formato de cadenas (F-String)
edad = 16
Nombre = 'Martin'
mensaje = f"Hola, me llamo {Nombre} y tengo \n{edad} años"
print (mensaje)
#Contar los carecteres de una cadena
texto = "¡Felicicdades por aun continuar en el CECY!"
cantidad_caracteres = len(texto)
print(cantidad_caracteres)
oracion = "Aprender python es divertido"
if "python" in oracion:
    print("Encontrado")
else:
    print("No esta")
#Validar contenido de una cadena
ncadena = "22"
print(ncadena.isalpha())#True
print(ncadena.isdigit())#Flase