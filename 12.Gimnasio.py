# 12. Gimnasio: promedio de rendimiento semanal 
# Registrar 5 personas en un gimnasio. 
# Por cada una pedir: 
# • nombre 
# • días asistidos en la semana 
# • minutos promedio entrenados por día 
# Clasificar: 
# • menos de 3 días → bajo compromiso 
# • 3 a 4 días → compromiso medio 
# • 5 o más → compromiso alto 
# Al final mostrar cuántas personas quedaron en cada categoría. 
# Practica: ciclos, contadores, condicionales.

print("===========================================")
print(     "Bienvenido al gimnasio!")
print("===========================================")

compromiso_bajo = 0
compromiso_medio = 0
compromiso_alto = 0     

for i in range(5):
    nombre = input(f"\nIngrese el nombre de la persona {i + 1}: ")
    dias_asistidos = int(input("Ingrese los días asistidos en la semana: "))
    minutos_entrenados = int(input("Ingrese los minutos promedio entrenados por día: "))

    if dias_asistidos < 3:
        compromiso_bajo += 1
    elif 3 <= dias_asistidos <= 4:
        compromiso_medio += 1
    else:
        compromiso_alto += 1    

print("\n================================")
print("Resultados del registro")
print("================================")
print(f"Personas con compromiso bajo: {compromiso_bajo}")
print(f"Personas con compromiso medio: {compromiso_medio}") 
print(f"Personas con compromiso alto: {compromiso_alto}")

