# 6. Parqueadero: cobro por horas 
# Pide cuántas horas estuvo un carro en un parqueadero. 
# Reglas: 
# • primera hora = 5000 
# • cada hora adicional = 3000 
# Muestra el total a pagar. 
# Practica: condicionales y operaciones.

print("===========================================")
print(     "Bienvenido al parqueadero!")
print("===========================================") 

h1 = 5000
ha = 3000
hora = int(input("Ingrese el número de horas que estuvo el carro en el parqueadero: "))

if hora <= 1:
    total = h1
    print(f"El total a pagar por {hora} hora(s) es: ${total}")
elif hora > 1:
    total = h1 + (ha * (hora - 1))
    print(f"El total a pagar por {hora} hora(s) es: ${total}")