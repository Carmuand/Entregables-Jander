# 9. Spa: servicio disponible 
# En un spa hay estos servicios: 
# • masaje 
# • facial 
# • manicure 
# Pide al usuario qué servicio desea y muestra un mensaje confirmando 
# si existe o no. 
# Practica: condicionales con texto.

print("===========================================")
print(        "Bienvenido al Spa!"            )         
print("===========================================")

servicio = input("Ingrese el servicio que desea (masaje, facial, manicure): ").lower()
if servicio == "masaje":
    print("Has elegido el servicio de masaje. ¡Disfrútalo!")
elif servicio == "facial":
    print("Has elegido el servicio de facial. ¡Disfrútalo!")
elif servicio == "manicure":
    print("Has elegido el servicio de manicure. ¡Disfrútalo!")
else:
    print("El servicio ingresado no está disponible.")