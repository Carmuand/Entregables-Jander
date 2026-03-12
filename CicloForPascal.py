n = int(input("¿Cuántas filas de Pascal quieres? "))

fila_anterior = [1] 

for i in range(n):
    print(fila_anterior)

    fila_nueva = [0] * (i + 2)
    fila_nueva[0] = 1
    fila_nueva[-1] = 1

    for i in range(1, i + 1):
        fila_nueva[i] = fila_anterior[i-1] + fila_anterior[i]

    fila_anterior = fila_nueva