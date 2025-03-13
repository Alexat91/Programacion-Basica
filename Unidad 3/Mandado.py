
 # Lista vacía para almacenar los productos
productos = []

while True:
    print("\n📋 LISTA DE COMPRAS📋")
    print("1. Definir cantidad de productos")
    print("2. Agregar productos")
    print("3. Ver productos")
    print("4. Eliminar productos")
    print("5. Salir")

    opcion = input("¿Qué deseas hacer? ")

    if opcion == "1":
        cantidad = input("📝 Escribe la cantidad de productos: ")
        if cantidad.isdigit() and 0 < int(cantidad) <= 5:
            print(f"✅ Puedes proceder con la elaboración de la lista.")
        else:
            print("❌ Ingresa un número válido entre 1 y 5.")

    elif opcion == "2":
        producto = input("📝 Escribe el producto a agregar: ")
        productos.append(producto)
        print(f"✅ Producto '{producto}' agregado.")

    elif opcion == "3":
        if not productos:
            print("📭 No hay productos en la lista.")
        else:
            print("\n📌 Lista de Productos:")
            for i, producto in enumerate(productos, 1):
                print(f"{i}. {producto}")

    elif opcion == "4":
        if not productos:
            print("📭 No hay productos para eliminar.")
        else:
            try:
                num = int(input("🗑️ Número del producto a eliminar: ")) - 1
                if 0 <= num < len(productos):
                    eliminado = productos.pop(num)
                    print(f"🗑️ Producto '{eliminado}' eliminado.")
                else:
                    print("❌ Número inválido.")
            except ValueError:
                print("❌ Ingresa un número válido.")

    elif opcion == "5":
        print("👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("❌ Opción inválida. Intenta de nuevo.")