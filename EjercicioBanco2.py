saldo1 = 100000   # Cuenta principal
saldo2 = 50000    # Cuenta secundaria (para cubrir comisiones)

sw = False

def calcular_comision(monto):
    return monto * 0.004  

while not sw:
    print("\n--- MENÚ ---")
    print(f"Cuenta 1: {saldo1:.2f}")
    print(f"Cuenta 2: {saldo2:.2f}")
    print("1. Retirar")
    print("2. Depositar")
    print("3. Pagar")
    print("4. Transferir")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ")

    if opcion == "1":
        try:
            monto = float(input("Ingrese el monto a retirar: "))
        except ValueError:
            print("Monto no válido.")
            continue

        if monto <= 0:
            print("No puedes ingresar valores negativos o 0.")
            continue

        if monto > saldo1:
            print("No tiene suficiente saldo en cuenta 1.")
            continue

        comision = calcular_comision(monto)

        if monto == saldo1:
            if saldo2 < comision:
                print("Cuenta 2 no tiene saldo para cubrir la comisión.")
                continue

            saldo1 -= monto
            saldo2 -= comision

            print("Retiro exitoso.")
            print(f"Comisión descontada de cuenta 2: {comision:.2f}")

        else:
            if saldo1 < (monto + comision):
                print("Saldo insuficiente para cubrir monto + comisión.")
                continue

            saldo1 -= (monto + comision)

            print("Retiro exitoso.")
            print(f"Comisión descontada de cuenta 1: {comision:.2f}")

    elif opcion == "2":
        try:
            monto = float(input("Ingrese el monto a depositar: "))
        except ValueError:
            print("Monto no válido.")
            continue

        if monto <= 0:
            print("El monto debe ser mayor que 0.")
            continue

        saldo1 += monto
        print("Depósito exitoso.")
        print(f"Nuevo saldo Cuenta 1: {saldo1:.2f}")


    elif opcion == "3":
        try:
            monto = float(input("Ingrese el monto a pagar: "))
        except ValueError:
            print("Monto no válido.")
            continue

        if monto <= 0:
            print("El monto debe ser mayor que 0.")
            continue

        if monto > saldo1:
            print("No tiene suficiente saldo.")
            continue

        saldo1 -= monto
        print("Pago exitoso.")
        print(f"Nuevo saldo Cuenta 1: {saldo1:.2f}")


    elif opcion == "4":
        cuenta_destino = input("Ingrese el número de cuenta destino: ")

        try:
            monto = float(input("Monto a transferir: "))
        except ValueError:
            print("Monto no válido.")
            continue

        if monto <= 0:
            print("El monto debe ser mayor que 0.")
            continue

        if monto > saldo1:
            print("Saldo insuficiente en cuenta 1.")
            continue

        comision = calcular_comision(monto)

        if monto == saldo1:
            if saldo2 < comision:
                print("Cuenta 2 no tiene saldo para cubrir la comisión.")
                continue

            saldo1 -= monto
            saldo2 -= comision

            print(f"Transferencia exitosa a la cuenta {cuenta_destino}")
            print(f"Comisión descontada de cuenta 2: {comision:.2f}")

        else:
            if saldo1 < (monto + comision):
                print("Saldo insuficiente para cubrir monto + comisión.")
                continue

            saldo1 -= (monto + comision)

            print(f"Transferencia exitosa a la cuenta {cuenta_destino}")
            print(f"Comisión descontada de cuenta 1: {comision:.2f}")

    elif opcion == "5":
        print("\nGracias por usar el sistema.")
        print(f"Saldo final Cuenta 1: {saldo1:.2f}")
        print(f"Saldo final Cuenta 2: {saldo2:.2f}")
        sw = True

    else:
        print("Opción no válida. Ingrese un número del 1 al 5.")
