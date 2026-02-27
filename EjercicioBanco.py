saldo = 1000
sw = False

while not sw:
    print("\nSaldo actual:", saldo)
    print("1. Retirar")
    print("2. Depositar")
    print("3. Pagar")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    if opcion == "1":
        try:
            monto = float(input("Ingrese el monto a retirar: "))
        except ValueError:
            print("Monto no válido. Por favor, ingrese un número.")
            continue

        if monto <= 0:
            print("No puedes ingresar valores negativos o 0.")
            continue

        if monto > saldo:
            print("No tiene suficiente saldo para retirar esa cantidad.")
        else:
            saldo -= monto
            print("Retiro exitoso. Nuevo saldo:", saldo)

    elif opcion == "2":
        try:
            monto = float(input("Ingrese el monto a depositar: "))
        except ValueError:
            print("Monto no válido. Por favor, ingrese un número.")
            continue

        if monto <= 0:
            print("El monto debe ser mayor que 0.")
            continue

        saldo += monto
        print("Depósito exitoso. Nuevo saldo:", saldo)

    elif opcion == "3":
        try:
            monto = float(input("Ingrese el monto a pagar: "))
        except ValueError:
            print("Monto no válido. Por favor, ingrese un número.")
            continue

        if monto <= 0:
            print("El monto debe ser mayor que 0.")
            continue

        if monto > saldo:
            print("No tiene suficiente saldo para pagar esa cantidad.")
        else:
            saldo -= monto
            print("Pago exitoso. Nuevo saldo:", saldo)

    elif opcion == "4":
        print("Gracias por usar el cajero automático. Saldo final:", saldo)
        sw = True

    else:
        print("Opción no válida. Ingrese un número del 1 al 4.")