# 17. Peluquería: agenda de atención 
# Una peluquería atiende 7 clientes al día. 
# Por cada cliente pedir: 
# • nombre 
# • servicio solicitado: corte, cepillado, tintura 
# • valor pagado 
# Al final mostrar: 
# • total del día 
# • cantidad de clientes por servicio 
# • servicio más solicitado 
# Practica: contadores, acumuladores, comparaciones. 

print("===========================================")
print(     "Bienvenido a la peluquería!")   
print("===========================================")

total_dia = 0
contador_corte = 0
contador_cepillado = 0
contador_tintura = 0

for i in range(0, 7, 1):
    nombre = input(f"\nIngrese el nombre del cliente {i + 1}: ")
    servicio = input("Ingrese el servicio solicitado (corte, cepillado, tintura): ").lower()
    valor_pagado = float(input("Ingrese el valor pagado por el servicio: "))

    total_dia += valor_pagado

    if servicio == "corte":
        contador_corte += 1
    elif servicio == "cepillado":
        contador_cepillado += 1
    elif servicio == "tintura":
        contador_tintura += 1
    else:
        print("Servicio no reconocido. Por favor, ingrese corte, cepillado o tintura.")
print("\n================================")
print("Resultados del día")
print("================================")
print(f"Total recaudado en el día: ${total_dia}")
print(f"Cantidad de clientes que solicitaron corte: {contador_corte}")
print(f"Cantidad de clientes que solicitaron cepillado: {contador_cepillado}")
print(f"Cantidad de clientes que solicitaron tintura: {contador_tintura}")

if contador_corte > contador_cepillado and contador_corte > contador_tintura:
    servicio_mas_solicitado = "corte"   
elif contador_cepillado > contador_corte and contador_cepillado > contador_tintura:
    servicio_mas_solicitado = "cepillado"
elif contador_tintura > contador_corte and contador_tintura > contador_cepillado:
    servicio_mas_solicitado = "tintura"
else:
    servicio_mas_solicitado = "No hay un servicio más solicitado, hay un empate."
print(f"El servicio más solicitado fue: {servicio_mas_solicitado}")
