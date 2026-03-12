# 11. Heladería: factura de varios clientes 
# Una heladería quiere registrar varios clientes hasta que el usuario decida salir. 
# Productos: 
# • cono = 3000 
# • vaso = 4000 
# • banana split = 9000 
# Por cada cliente: 
# • pedir producto 
# • pedir cantidad 
# • calcular total 
# Al final mostrar: 
# • total vendido 
# • cuántos clientes se atendieron 
# • cuál producto se pidió más veces 
# Practica: ciclos, acumuladores, contadores.

print("===========================================")   
print(      "Bienvenido a la heladería!")
print("===========================================")

cono = 3000
vaso = 4000
banana_split = 9000 

total_vendido = 0
clientes_atendidos = 0
contador_cono = 0
contador_vaso = 0
contador_banana_split = 0

while True:
    print("\nProductos disponibles:")
    print("\n1. Cono")
    print("2. Vaso")
    print("3. Banana Split")
    print("4. Salir")

    producto_elegido = int(input("Ingrese el número del producto que desea comprar (1-4): "))

    if producto_elegido == 4:
        break

    cantidad = int(input("Ingrese la cantidad que desea comprar: "))

    if producto_elegido == 1:
        total_vendido += cono * cantidad
        contador_cono += cantidad

    elif producto_elegido == 2:
        total_vendido += vaso * cantidad
        contador_vaso += cantidad

    elif producto_elegido == 3:
        total_vendido += banana_split * cantidad
        contador_banana_split += cantidad

    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")
        continue

    clientes_atendidos += 1

print("\n================================")
print("Resumen del día")
print("================================")

print("Total vendido:", total_vendido)
print("Clientes atendidos:", clientes_atendidos)

if contador_cono > contador_vaso and contador_cono > contador_banana_split:
    print("Producto más vendido: Cono")

elif contador_vaso > contador_cono and contador_vaso > contador_banana_split:
    print("Producto más vendido: Vaso")

elif contador_banana_split > contador_cono and contador_banana_split > contador_vaso:
    print("Producto más vendido: Banana Split")

else:
    print("Hay empate en los productos más vendidos.")
