
# Lista vacía para almacenar los productos
lista_compras = []

respuesta = input("¿Deseas realizar el mandado? (sí/no): ").lower()
if respuesta == "si":
printf("¿Cuantos productos deseas comprar")
     else:
printf("Cerrando el programa")

print("🛒 Lista de Compras 🛒")

# Agregar productos
producto1 = input("Agrega el primer producto: ")
lista_compras.append(producto1)

producto2 = input("Agrega el segundo producto: ")
lista_compras.append(producto2)

producto3 = input("Agrega el tercer producto: ")
lista_compras.append(producto3)

# Mostrar la lista completa
print("\n📌 Tu lista de compras es:")
for producto in lista_compras:
    print(f"- {producto}")

print("\n✅ ¡Lista creada con éxito!")