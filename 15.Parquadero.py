# 15. Parqueadero: control de vehículos 
# Registrar 8 vehículos en un parqueadero. 
# Por cada uno pedir: 
# • placa 
# • tipo: carro o moto 
# • horas parqueado 
# Tarifas: 
# • carro: 4000 por hora 
# • moto: 2000 por hora 
# Al final mostrar: 
# • total recaudado 
# • cuántos carros ingresaron 
# • cuántas motos ingresaron 
# • cuál vehículo pagó más 
# Practica: ciclos, máximos, acumuladores.

print("===========================================")
print(     "Bienvenido al parqueadero!")
print("===========================================")

total_recaudado = 0
contador_carros = 0
contador_motos = 0  

for i in range(0, 8, 1):
    placa = input(f"\nIngrese la placa dell vehiculo {i + 1}: ")
    tipo = input("Ingrese el tipo de vehiculo (carro/moto): ").lower()
    horas_parqueado = int(input("Ingrese las horas parqueado: "))
    if tipo == "carro":
        tarifa = 4000
        contador_carros += 1
    elif tipo == "moto":
        tarifa = 2000
        contador_motos += 1 
    else:
        print("Tipo de vehículo no válido. Por favor, ingrese 'carro' o 'moto'.")
        continue
    total_pago = tarifa * horas_parqueado
    total_recaudado += total_pago   
    print(f"El vehículo con placa {placa} pagó: ${total_pago}")
print("\n================================")
print("Resultados del registro")    
print("================================")
print(f"Total recaudado: ${total_recaudado}")   
print(f"Cantidad de carros ingresados: {contador_carros}")
print(f"Cantidad de motos ingresadas: {contador_motos}")    
