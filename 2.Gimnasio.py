# 2. Gimnasio: acceso por edad 
# Un gimnasio ofrece clases según la edad: 
# • menor de 13 → no puede ingresar 
# • de 13 a 17 → clase juvenil 
# • de 18 a 59 → clase general 
# • 60 o más → clase senior 
# pedidos. 
# Pide la edad de una persona y muestra a qué grupo pertenece. 
# Practica: if, elif, else.

print("===========================================")
print(        "Bienvenido al gimnasio!")  
print("===========================================")                  

edad = int(input("Ingrese su edad: "))
if edad < 13:
    print("Lo sentimos, no puede ingresar al gimnasio.")
elif 13 <= edad <=17:
    print("Bienvenido a la clase juvenil. ")
elif 18 <= edad <= 59:
    print("Bienvenido a la clase general.")
else:
    print("Bienvenido a la clase senior.")