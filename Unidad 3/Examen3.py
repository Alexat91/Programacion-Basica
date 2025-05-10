import time 
import random 
import os 
from Archivos import guardar_diccionarios_en_csv, leer_diccionarios_de_csv

alumnos = []
calificaciones = {}
archivo = "alumnos.csv"

def generar_id():
    return random.randint(1000, 9999)

# Iniciar temporizador
inicio = time.perf_counter()

while True:
    print("Menú de opciones:")
    print("1. Agregar alumno")
    print("2. Eliminar alumno")
    print("3. Mostrar lista de alumnos")
    print("4. Buscar alumno por ID")
    print("5. Asignar calificación a un alumno")
    print("6. Mostrar calificaciones")
    print("7. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1": 
        nombre = input("Ingrese el nombre del alumno: ")
        id_alumno = generar_id()
        alumnos.append({"id": id_alumno, "nombre": nombre})
        calificaciones[id_alumno] = [] 
        print(f"Alumno {nombre} agregado con ID {id_alumno}.")
    
    elif opcion == "2": 
        id_buscar = int(input("Ingrese el ID del alumno a eliminar: "))
        for alumno in alumnos:
            if alumno["id"] == id_buscar:
                alumnos.remove(alumno)
                del calificaciones[id_buscar] 
                print("Alumno eliminado.")
                break
        else:
            print("ID no encontrado.")
    
    elif opcion == "3":
        print("Lista de alumnos:")
        for alumno in alumnos:
            print(f"ID: {alumno['id']} - Nombre: {alumno['nombre']}")
    
    elif opcion == "4": 
        id_buscar = int(input("Ingrese el ID del alumno: "))
        for alumno in alumnos:
            if alumno["id"] == id_buscar:
                print(f"Alumno encontrado: {alumno['nombre']}, ID: {alumno['id']}")
                break
        else:
            print("ID no encontrado.")
    
    elif opcion == "5":  
        id_buscar = int(input("Ingrese el ID del alumno: "))
        if id_buscar in calificaciones:
            calificacion = float(input("Ingrese la calificación: "))
            calificaciones[id_buscar].append(calificacion)
            print("Calificación asignada.")
        else:
            print("ID no encontrado.")
    
    elif opcion == "6":  
        print("Calificaciones de los alumnos:")
        for alumno in alumnos:
            id_alumno = alumno["id"]
            print(f"ID: {id_alumno} - {alumno['nombre']} - Calificaciones: {calificaciones[id_alumno]}")
    
    elif opcion == "7": 
        print("Saliendo...")
        break
    
    else:
        print("Opción inválida.")

    guardar_diccionarios_en_csv(alumnos, calificaciones)
    time.sleep(1)

fin = time.perf_counter()
duracion = fin - inicio
print(f"\nTiempo total de ejecución: {duracion:.2f} segundos.")
