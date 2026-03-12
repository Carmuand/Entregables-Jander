# 19. Tienda de ropa deportiva: inventario crítico 
# Registrar 10 productos. 
# Por cada producto pedir: 
# • nombre 
# • cantidad disponible 
# Clasificar: 
# • 0 → agotado 
# • 1 a 5 → stock bajo 
# • 6 o más → stock normal 
# Al final mostrar: 
# • cuántos están agotados 
# • cuántos tienen stock bajo 
# • cuántos están normales 
# Practica: clasificación por rangos, ciclo.

print("===========================================")
print(     "Bienvenido a la tienda de ropa deportiva!")
print("===========================================")

agotados = 0
stock_bajo = 0
stock_normal = 0

for i in range(10):
    nombre = input(f"\nIngrese el nombre del producto {i + 1}: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))

    if cantidad == 0:
        agotados += 1
    elif 1 <= cantidad <= 5:
        stock_bajo += 1
    else:
        stock_normal += 1
print("\n================================")
print("Resultados del inventario")
print("================================")
print(f"Productos agotados: {agotados}")
print(f"Productos con stock bajo: {stock_bajo}")
print(f"Productos con stock normal: {stock_normal}")
