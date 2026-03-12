# 7. Peluquería: turno del día 
# Pide la hora de llegada de un cliente en formato entero de 0 a 23. 
# Mostrar: 
# • mañana si está entre 6 y 11 
# • tarde si está entre 12 y 17 
# • noche si está entre 18 y 22 
# • fuera de horario en cualquier otro caso 
# Practica: rangos con condicionales.

print("===========================================")    
print(     "Bienvenido a la peluquería!")
print("===========================================")

hora = int(input("Ingrese la hora de llegada (0-23): "))
if 6 <= hora <= 11:
    print("Turno de la mañana.")    
elif 12 <= hora <= 17:
    print("Turno de la tarde.")
elif 18 <= hora <= 22:
    print("Turno de la noche.")
else:
    print("Fuera de horario.")