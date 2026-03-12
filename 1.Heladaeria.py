# 1. Heladería: sabor más pedido 
# Una heladería quiere registrar 5 pedidos Por cada cliente, el programa debe pedir el sabor elegido: 
# • vainilla 
# • chocolate 
# • fresa 
# Al final debe mostrar cuántas veces se pidió cada sabor. 
# Practica: ciclos, condicionales, contadores. 

print("====================================")
print("    Bienvenido a la heladería!")
print("====================================")

s1 = "Vainilla"
s2 = "Chocolate"
s3 = "Fresa"

ts1 = 0
ts2 = 0
ts3 = 0

def pedir_sabores():
    print("Sabores disponibles:")
    print("\n1. Vainilla")
    print("2. Chocolate")
    print("3. Fresa")
    
    print("==================================================")

for i in range(0, 5, 1):
    print(f"\n---- Cliente ----")
    pedir_sabores()
    sabor_elegido = int(input("Ingrese el número del sabor elegido (1-3): "))

    if sabor_elegido == 1:
        ts1 += 1
    elif sabor_elegido == 2:
        ts2 += 1 
    elif sabor_elegido == 3:
        ts3 += 1
    else: 
        print("Opción no válida. Por favor, elija un número entre 1 y 3.")

    print("\n==================================================")
    print("Resultados de los pedidos:")
    print(f"Vainilla: {ts1}")
    print(f"Chocolate: {ts2}")
    print(f"Fresa: {ts3}")