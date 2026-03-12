# 13. Cafetería: descuento por consumo 
# Registrar varios pedidos en una cafetería hasta que el usuario escriba 
# “salir”. 
# Productos: 
# • café = 4000 
# • capuchino = 7000 
# • pastel = 6000 
# Reglas: 
# • si la compra supera 20000, aplicar 10% de descuento 
# • si no, cobrar normal 
# Mostrar total por cliente y al final total acumulado del día. 
# Practica: menú simple, ciclos, descuentos.

print("===========================================")
print(     "Bienvenido al Cafeteria!")
print("===========================================")

cafe = 4000
capuchino = 7000
pastel = 6000

total_acumulado = 0 

opcion = "Salir"

while opcion == "Salir":
    print("\nProductos disponibles:")
    print("\n1. Cafe")
    print("2. Capuchino")
    print("3. Pastel")
    print("4. Salir")

    opcion = str(input("Ingrese el producto que desea comprar: "))

    if opcion == "Salir":
        break

    cantidad = int(input("Ingrese la cantidad que desea comprar: "))

    if opcion == "Cafe":
        total = cafe * cantidad
    elif opcion == "Capuchino":
        total = capuchino * cantidad
    elif opcion == "Pastel":
        total = pastel * cantidad
    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")
        continue

    if total > 20000:
        descuento = total * 0.10
        total_con_descuento = total - descuento
        print(f"Total a pagar por este pedido con descuento: ${total_con_descuento:.2f}")
        total_acumulado += total_con_descuento
    else:
        print(f"Total a pagar por este pedido: ${total}")
        total_acumulado += total

print(f"\nTotal acumulado del día: ${total_acumulado}")