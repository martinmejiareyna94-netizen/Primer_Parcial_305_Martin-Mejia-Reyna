#Creando un diccionario en python
persona = {
    "Nombre":"Martin",
    "Edad":16,
    "Profecion":"Ingeniero",
    "Estudiante":True
}
print(persona)
#Accediendo a un valor especifico
print(persona["Profecion"])
#Se puede usar el metodo .get().
#Es util porque no da error si la clave no existe.
print(persona.get("Edad"))
#Modificar un valor existente
persona["Edad"] = 16
print(persona.get("Edad"))
#Agregar un par(clave:calor)
persona["Ciudad"] = "México"
print(persona)
#Recorrer un diccionario con un bucle
for clave,valor in persona.items():
    print(f"{clave}:{valor}")