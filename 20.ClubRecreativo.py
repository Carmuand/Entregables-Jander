# 20. Club recreativo: control de membresías 
# Registrar varias personas en un club. 
# Por cada una pedir: 
# • nombre 
# • edad 
# • tipo de plan: basico, premium, familiar 
# Reglas: 
# • basico = 50000 
# • premium = 90000 
# • familiar = 130000 
# Además: 
# • si la persona es menor de 18, mostrar “registro juvenil” 
# • si tiene 60 o más, mostrar “beneficio senior” 
# Al final mostrar: 
# • total recaudado 
# • cantidad de personas por plan 
# • plan más vendido 
# Practica: condicionales, contadores, acumuladores.

print("===========================================")
print(     "Bienvenido al club recreativo!")      
print("===========================================")

total_recaudado = 0 
contador_basico = 0
contador_premium = 0
contador_familiar = 0

opcion = "salir"

while opcion == "salir":
    nombre = input("\nIngrese el nombre de la persona (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    edad = int(input("Ingrese la edad de la persona: "))
    tipo_plan = input("Ingrese el tipo de plan (basico, premium, familiar): ").lower()

    if tipo_plan == "basico":
        costo = 50000
        contador_basico += 1
    elif tipo_plan == "premium":
        costo = 90000
        contador_premium += 1
    elif tipo_plan == "familiar":
        costo = 130000
        contador_familiar += 1
    else:
        print("Tipo de plan no válido. Por favor, ingrese basico, premium o familiar.")
        continue

    total_recaudado += costo

    if edad < 18:
        print("Registro juvenil")
    elif edad >= 60:
        print("Beneficio senior")
print("\n================================")
print("Resultados del registro")
print("================================")
print(f"Total recaudado: ${total_recaudado}")
print(f"Cantidad de personas con plan basico: {contador_basico}")
print(f"Cantidad de personas con plan premium: {contador_premium}")
print(f"Cantidad de personas con plan familiar: {contador_familiar}")
if contador_basico > contador_premium and contador_basico > contador_familiar:
    plan_mas_vendido = "basico"
elif contador_premium > contador_basico and contador_premium > contador_familiar:   
    plan_mas_vendido = "premium"
elif contador_familiar > contador_basico and contador_familiar > contador_premium:
    plan_mas_vendido = "familiar"
else:    plan_mas_vendido = "No hay un plan más vendido, hay un empate."
print(f"El plan más vendido fue: {plan_mas_vendido}")
