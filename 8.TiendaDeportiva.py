# 8. Tienda deportiva: contar productos caros 
# Pide el precio de 6 productos deportivos.
# Al final indica cuántos cuestan más de 100000. 
# Practica: ciclo, contador, condicional. 

print("===========================================")    
print(     "Bienvenido a la peluquería!")
print("===========================================")

contador = 0
for i in range(6):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    if precio > 100000:
        contador += 1
print(f"El número de productos que cuestan más de 100000 es: {contador}")

