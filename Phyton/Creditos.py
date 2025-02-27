creditos = int(input("Ingrese la cantidad de creditos que tienes: "))
if creditos >= 80 and creditos < 120:
     print("Puedes hacer tu servivio social.")
if creditos >= 120:
    print("Puedes hacer la residencia.")
if creditos < 80:
    print("No puedes hacer ninguna de las dos.")
