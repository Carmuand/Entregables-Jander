saldo = 1000

sw = False
while (not sw):
    print("Saldo actual:", saldo)
    opcion = input("¿Desea retirar dinero? (s/n): ")
    
    if opcion.lower() == 's':
        try:            
            monto = float(input("Ingrese el monto a retirar: "))
        except ValueError:
            print("Monto no válido. Por favor, ingrese un número.")
            continue

        if monto > saldo:
            print("No tiene suficiente saldo para retirar esa cantidad.")
        else:
            saldo -= monto
            print("Retiro exitoso. Nuevo saldo:", saldo)
    elif opcion.lower() == 'n':
        print("Gracias por usar el cajero automático. Saldo final:", saldo)
    else:
        print("Opción no válida. Por favor, ingrese 's' o 'n'.")