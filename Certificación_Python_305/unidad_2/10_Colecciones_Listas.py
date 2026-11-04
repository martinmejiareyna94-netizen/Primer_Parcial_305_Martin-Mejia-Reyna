carrito = []
n_productos  = int(input("Ingresa el numero de productos"))
for i in range(n_productos):
    producto = input("Ingresa el produto a tu carrito")
    carrito.append(producto)
print("Lista creada correctamente")
print(f"Tu carrito contiene{carrito}")
carrito[0]="barritas"
print(f"Tu carrito contiene{carrito}")