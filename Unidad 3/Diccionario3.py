#Diccionario 3

Tec = {
"Lupita":{ "edad": 18, "materia":"Calculo", "promedio": 9.8, "maestro":"Marlem"},	
"Aaron":{ "edad": 18, "materia":"Algebra","promedio": 7.8, "maestro":"Jorge Luis"},	
"Saba":{ "edad": 19, "materia": "Estadistica","promedio": 9.8, "maestro":"Guilleromo"}	,
"Manuel":{ "edad": 18, "materia":"Contabilidad","promedio": 8.9, "maestro":"Martha"},
"Victor":{ "edad": 18, "materia":"Programacion","promedio": 7.8, "maestro":"Eduardo"},
"Cristian":{ "edad": 18, "materia":"Programacion","promedio": 9.8, "maestro":"Eduardo"},	
"Oswaldo":{ "edad": 18, "materia":"Materiales","promedio": 7.8, "maestro":"Enrique"},
"Enrique":{ "edad": 18, "materia":"Calculo","promedio": 7.8, "maestro":"Marlem"},
} 

# Imprimir el diccionario completo
print("Tec:")
for nombre, edad, materia, promedio, maestro in Tec.items():
    print(f"{nombre} tiene {edad} años, en {maeria} tiene  {promedio} su {maestro } es {nombre} ")
