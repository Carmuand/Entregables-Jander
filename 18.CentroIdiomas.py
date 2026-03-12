# 18. Centro de idiomas: evaluación de estudiantes 
# Registrar varios estudiantes de un curso de inglés. 
# Por cada uno pedir: 
# • nombre 
# • nota speaking 
# • nota listening 
# • nota reading 
# Calcular promedio simple y clasificar: 
# • menor de 60 → bajo 
# • 60 a 79 → medio 
# • 80 o más → alto 
# Al final mostrar: 
# • promedio general del grupo 
# • mejor estudiante 
# • cuántos quedaron en cada nivel 
# Practica: promedios, máximos, contadores. 

print("===========================================")
print(     "Bienvenido al centro de idiomas!")                  
print("===========================================")

total_promedio = 0
contador_estudiantes = 0    
compromiso_bajo = 0
compromiso_medio = 0    
compromiso_alto = 0
mejor_estudiante = ""
mejor_promedio = 0

opcion = "salir"

while opcion == "salir":
    nombre = input(f"\nIngrese el nombre del estudiante {contador_estudiantes + 1} (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    nota_speaking = float(input("Ingrese la nota de speaking: "))
    nota_listening = float(input("Ingrese la nota de listening: "))
    nota_reading = float(input("Ingrese la nota de reading: "))

    promedio = (nota_speaking + nota_listening + nota_reading) / 3
    total_promedio += promedio
    contador_estudiantes += 1

    if promedio < 60:
        compromiso_bajo += 1
    elif 60 <= promedio < 80:
        compromiso_medio += 1
    else:
        compromiso_alto += 1

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre
print("\n================================")
print("Resultados del curso")
print("================================")
if contador_estudiantes > 0:
    promedio_general = total_promedio / contador_estudiantes
    print(f"Promedio general del grupo: {promedio_general:.2f}")
else:
    print("No se registraron estudiantes.")
print(f"Mejor estudiante: {mejor_estudiante} con un promedio de {mejor_promedio:.2f}")
print(f"Cantidad de estudiantes con compromiso bajo: {compromiso_bajo}")
print(f"Cantidad de estudiantes con compromiso medio: {compromiso_medio}")
print(f"Cantidad de estudiantes con compromiso alto: {compromiso_alto}")
