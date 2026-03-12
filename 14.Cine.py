# 14. Cine: control de sala 
# Pedir la capacidad total de una sala de cine y luego registrar cuántas 
# personas ingresan. 
# Por cada persona pedir edad y clasificar: 
# • niño 
# • adulto 
# • adulto mayor 
# Al final mostrar: 
# • total de personas ingresadas 
# • cuántos niños 
# • cuántos adultos 
# • cuántos adultos mayores 
# • si la sala se llenó o no 
# Practica: ciclos con límite, contadores.

print("===========================================")
print(     "Bienvenido al cine!")       
print("===========================================")

capacidad_sala = int(input("Ingrese la capacidad total de la sala: "))
personas_ingresadas = 0 
contador_ninos = 0
contador_adultos = 0
contador_adultos_mayores = 0
while personas_ingresadas < capacidad_sala:
    edad = int(input("Ingrese la edad de la persona que ingresa: "))

    if edad < 12:
        contador_ninos += 1
    elif 12 <= edad <= 59:
        contador_adultos += 1
    else:
        contador_adultos_mayores += 1

    personas_ingresadas += 1

print("===========================================")
print(     "Resumen de ingresos:")       
print("===========================================")
print(f"Total de personas ingresadas: {personas_ingresadas}")
print(f"Niños: {contador_ninos}")
print(f"Adultos: {contador_adultos}")
print(f"Adultos mayores: {contador_adultos_mayores}")
if personas_ingresadas == capacidad_sala:
    print("La sala se llenó.")
else:
    print("La sala no se llenó.")