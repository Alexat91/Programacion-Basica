texto = input("Introduce un texto para analizar: ")

contador_vocales = 0
contador_consonantes = 0
contador_numeros = 0
contador_otros = 0

for caracter in texto:
    caracter = caracter.lower()  

    if caracter in "aeiou":
        contador_vocales += 1
    elif caracter.isalpha(): 
        contador_consonantes += 1
    elif caracter.isdigit():
        contador_numeros += 1
    else:
        contador_otros += 1  


print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")
print(f"Números: {contador_numeros}")
print(f"Otros caracteres: {contador_otros}")