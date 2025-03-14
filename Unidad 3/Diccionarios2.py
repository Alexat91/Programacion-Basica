# Diccionarios2.py

# Crear un diccionario con más de dos valores por clave
estudiantes = {
    "Juan": {"edad": 20, "carrera": "Ingeniería", "promedio": 8.5},
    "Ana": {"edad": 22, "carrera": "Medicina", "promedio": 9.0},
    "Luis": {"edad": 21, "carrera": "Derecho", "promedio": 7.8},
    "Maria": {"edad": 23, "carrera": "Arquitectura", "promedio": 8.9}
}

# Imprimir el diccionario completo
print("Diccionario de estudiantes:")
for nombre, detalles in estudiantes.items():
    print(f"{nombre}: {detalles}")

# Acceder a los valores de un estudiante específico
nombre_estudiante = "Ana"
if nombre_estudiante in estudiantes:
    detalles = estudiantes[nombre_estudiante]
    print(f"\nDetalles de {nombre_estudiante}:")
    print(f"Edad: {detalles['edad']}")
    print(f"Carrera: {detalles['carrera']}")
    print(f"Promedio: {detalles['promedio']}")
else:
    print(f"\nEstudiante {nombre_estudiante} no encontrado en el diccionario.")