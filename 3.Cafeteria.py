# 3. Cafetería: total de una compra sencilla 
# En una cafetería venden: 
# • café = 4000 
# • té = 3500 
# • jugo = 5000 
# Pide al usuario qué bebida quiere y cuántas unidades desea comprar. 
# Luego muestra el total a pagar. 
# Practica: condicionales, variables, multiplicación.

print("===========================================")
print(        "Bienvenido al Cafeteria"            )  
print("===========================================")                  

cafe = 4000
te = 3500
jugo = 5000

print("Bebidas disponibles:")
print("\n1. Café")
print("2. Té")
print("3. Jugo")

bebida_elegida = int(input("Ingrese el número de la bebida que desea comprar (1-3): "))
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

if bebida_elegida == 1:
    total = cafe * cantidad
    print(f"El total a pagar por {cantidad} cafe(s) es: ${total}")
elif bebida_elegida == 2:
    total = te * cantidad
    print(f"El total a pagar por {cantidad} te(s) es: ${total}")
elif bebida_elegida == 3:
    total = jugo * cantidad
    print(f"El total a pagar por {cantidad} jugo(s) es: ${total}")
else:
    print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")