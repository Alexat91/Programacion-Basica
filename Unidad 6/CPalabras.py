def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

nombre_programa = input("Introduce el nombre del programa: ")
print(f"Has iniciado el programa: {nombre_programa}")

texto_usuario = input("Escribe una frase o texto: ")

cantidad_palabras = contar_palabras(texto_usuario)

print(f"El texto contiene {cantidad_palabras} palabras.")
