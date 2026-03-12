# 4. Cine: entrada según edad 
# El precio de la entrada cambia así: 
# • niños menores de 12 → 8000 
# • adultos de 12 a 59 → 12000 
# • mayores de 60 → 9000 
# Pide la edad del cliente y muestra cuánto debe pagar. 
# Practica: condicionales. 

print("===========================================")
print(        "Bienvenido al cine!")
print("===========================================")   

edad = int(input("Ingrese su edad:"))
if edad < 12:
    print("El precio de la entrada es: $8000")
elif 12 <= edad <= 59:
    print("El precio de la entrada es: $12000")
else:
    print("El precio de la entrada es: $9000")
