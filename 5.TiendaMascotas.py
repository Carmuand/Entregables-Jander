# 5. Tienda de mascotas: alimento por tipo de animal 
# Pide el tipo de mascota: 
# • perro 
# • gato 
# • conejo 
# Luego muestra una recomendación de alimento según el animal. 
# Practica: comparaciones con texto.

print("===========================================")
print(     "Bienvenido a la tienda de mascotas!")
print("===========================================")   

m1 = "Perro"
m2 = "Gato"
m3 = "Conejo"

def pedir_mascota():
    print("Tipos de mascotas disponibles:")
    print("\n1. Perro")
    print("2. Gato")
    print("3. Conejo")
    
    print("==================================================")

    opcion = str(input("Ingrese el tipo de mascota: "))
    return opcion

def recomendar_alimento(opcion):

    if opcion == "Perro":
        print("\nAlimentos recomendados para Perro:")
        print("- Croquetas para perro")
        print("- Carne con arroz")
        print("- Galletas caninas")

    elif opcion == "Gato":
        print("\nAlimentos recomendados para Gato:")
        print("- Concentrado para gato")
        print("- Atún")
        print("- Pollo cocido")

    elif opcion == "Conejo":
        print("\nAlimentos recomendados para Conejo:")
        print("- Heno")
        print("- Zanahorias")
        print("- Hojas verdes")

    else:
        print("Lo sentimos no tenemos recomendaciones para este tipo de mascotas")

opcion_mascota = pedir_mascota()
recomendar_alimento(opcion_mascota)



