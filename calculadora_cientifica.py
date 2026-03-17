def pedir_numero(mensaje):
    valido = False
    while not valido:
        try:
            valor_str = input(mensaje).replace(",", ".").strip() 
            valor = float(valor_str)
            valido = True
        except ValueError:
            print("⚠ Debes ingresar un número válido.")
        return valor

def pedir_opcion_calculo(opciones):
    print("\n  ¿Qué desea calcular?")
    for i, nombre in enumerate(opciones, 1):
        print(f"{i}. {nombre}")

    opcion = 0
    while opcion < 1 or opcion > len(opciones):
        try:
            opcion = int(input(f"  Elige una opción (1–{len(opciones)}): "))
            if opcion < 1 or opcion > len(opciones):
                print(f"⚠ Opción fuera de rango. Elige entre 1 y {len(opciones)}.")
        except ValueError:
            print("⚠ Ingresa un número entero válido.")
    return opcion
            
def resolver_figura(opcion):
    if opcion == 1:
        circunferencia()
    elif opcion == 2:
        trapecio()
    elif opcion == 3:
        rectangulo()
    elif opcion == 4:
        triangulo_general()
    elif opcion == 5:
        triangulo_rectangulo()
    elif opcion == 6:
        esfera()
    elif opcion == 7:
        cubo()
    elif opcion == 8:
        cilindro()
    elif opcion == 9:
        cono()
    elif opcion == 10:
        salir()

# ══════════════════════════════════════════════════
#           FIGURAS 2D (PLANAS)
# ══════════════════════════════════════════════════

PI = 3.14159
resultados = []
sistema = ""
unidad_longitud = ""
unidad_area = ""
unidad_volumen = ""

# Funciones para calcular áreas y perímetros de figuras planas
#1. Circunferencia: área y perímetro

def circunferencia():  
        opcion = pedir_opcion_calculo(["Area", "Perímetro", "Ambos"])
                                       
        radio = -1
        while radio <= 0:
            radio = pedir_numero("  Ingresa el radio de la circunferencia: ")
        if radio <= 0:
            print("⚠ Error: El radio no puede ser menor que 0.")

        Area = PI * radio ** 2
        Perimetro = 2 * PI * radio

        if opcion == 1:
            print(f"Área de la circunferencia: {Area:.2f} {unidad_area}")
            resultados.append(f"Circunferencia -> radio={radio} {unidad_longitud}, area={Area:.2f} {unidad_area}")
        elif opcion == 2:
            print(f"Perímetro de la circunferencia: {Perimetro:.2f} {unidad_longitud}")
            resultados.append(f"Circunferencia -> radio={radio} {unidad_longitud}, perimetro={Perimetro:.2f} {unidad_longitud}")
        elif opcion == 3:
            print(f"Área de la circunferencia: {Area:.2f} {unidad_area}")
            print(f"Perímetro de la circunferencia: {Perimetro:.2f} {unidad_longitud}")
            resultados.append(f"Circunferencia -> radio={radio} {unidad_longitud}, area={Area:.2f} {unidad_area}, perimetro={Perimetro:.2f} {unidad_longitud}")


# 2. Trapecio: área y perímetro

def trapecio():
    opcion = pedir_opcion_calculo(["Área", "Perímetro", "Ambos"])
                                   
    Base = 0
    while Base <= 0:
        Base = pedir_numero("Ingresa la Base mayor del trapecio: ")
        if Base <= 0:
            print("⚠ Error: El valor no puede ser menor que 0. ")
        base = Base
        while base <= 0 or base >= Base:
            base = pedir_numero("Ingresa la base menor del trapecio: ")
            if base <= 0 or base >= Base:
                print("⚠ Error: Debe ser mayor que 0 y menor que la base mayor.")
        altura = 0
        while altura <= 0:
            altura = pedir_numero("Ingresa la altura del trapecio: ")
            if altura <= 0:
                print("⚠ Error: El valor no puede ser menor que 0.")
        Lado1 = 0
        while Lado1 <= 0:
            Lado1 = pedir_numero("Ingresa el Lado 1 del trapecio: ")
            if Lado1 <= 0:
                print("⚠ Error: El valor no puede ser menor que 0.")
        Lado2 = 0
        while Lado2 <= 0:
            Lado2 = pedir_numero("Ingresa el Lado 2 del trapecio: ")
            
            if Lado2 <= 0:
                print("⚠ Error: El valor no puede ser menor que 0.")
        
            Perimetro = Base + base + Lado1 + Lado2
            Area = ((Base + base) /2) * altura

        if opcion == 1:
            print(f"Área del trapecio: {Area:.2f} {unidad_area}")
            resultados.append(f"Trapecio -> BaseMayor={Base} {unidad_longitud}, BaseMenor={base} {unidad_longitud}, altura={altura} {unidad_longitud}, area={Area:.2f} {unidad_area}")
        elif opcion == 2:
            print(f"Perímetro del trapecio: {Perimetro:.2f} {unidad_longitud}")
            resultados.append(f"Trapecio -> BaseMayor={Base} {unidad_longitud}, BaseMenor={base} {unidad_longitud}, Lado1={Lado1} {unidad_longitud}, Lado2={Lado2} {unidad_longitud}, perimetro={Perimetro:.2f} {unidad_longitud}")
        elif opcion == 3:
            print(f"Área del trapecio: {Area:.2f} {unidad_area}")
            print(f"Perímetro del trapecio: {Perimetro:.2f} {unidad_longitud}")
            resultados.append(f"Trapecio -> BaseMayor={Base} {unidad_longitud}, BaseMenor={base} {unidad_longitud}, altura={altura} {unidad_longitud}, area={Area:.2f} {unidad_area}, perimetro={Perimetro:.2f} {unidad_longitud}")

# 3. Retángulo: área y perímetro

def rectangulo():
    opcion = pedir_opcion_calculo(["Área", "Perímetro", "Ambos"])
                                   
    base = 0
    while base <= 0:
        base = pedir_numero("Ingresa la base del rectángulo: ")
        if base <= 0:
            print("⚠ Error: El valor no puede ser menor que 0. ")
        altura = 0
        while altura <= 0:
            altura = pedir_numero("Ingresa la altura del rectangulo: ")
            if altura <= 0:
                print("⚠ Error: El valor no puede ser menor que 0.")
        
    Area = base * altura
    Perimetro = 2 * (base +altura)

    if opcion == 1:
        print(f"Área del rectángulo: {Area:.2f} {unidad_area}")
        resultados.append(f"Rectangulo -> base={base} {unidad_longitud}, altura={altura} {unidad_longitud}, area={Area:.2f} {unidad_area}")
    elif opcion == 2:
        print(f"Perímetro del rectángulo: {Perimetro:.2f} {unidad_longitud}")
        resultados.append(f"Rectangulo -> base={base} {unidad_longitud}, altura={altura} {unidad_longitud}, perimetro={Perimetro:.2f} {unidad_longitud}")
    elif opcion == 3:
        print(f"Área del rectángulo: {Area:.2f} {unidad_area}")
        print(f"Perímetro del rectángulo: {Perimetro:.2f} {unidad_longitud}")
        resultados.append(f"Rectangulo -> base={base} {unidad_longitud}, altura={altura} {unidad_longitud}, area={Area:.2f} {unidad_area}, perimetro={Perimetro:.2f} {unidad_longitud}")

# 4. Triángulo general: área, perimetro y semiperimetro

def triangulo_general():
    opcion = pedir_opcion_calculo(["Área", "Perímetro", "Ambos"])
                                   
    ladoa = 0
    while ladoa <= 0:
        ladoa = pedir_numero("Ingrese el lado a del triángulo: ")
        if ladoa <= 0:
            print("⚠ Error: El valor no puede ser menor que 0.")

        ladob = 0
        while ladob <= 0:
            ladob = pedir_numero("Ingrese el lado b del triángulo: ")
            if ladob <= 0:
                print("⚠ Error: El valor no puede ser menor que 0.")

        ladoc = 0
        while ladoc <= 0 or ladoc >= ladoa + ladob or ladoa >= ladob + ladoc or ladob >= ladoa + ladoc:
            ladoc = pedir_numero("Ingrese el lado c del triángulo: ")
            if ladoc <= 0 or ladoc >= ladoa + ladob or ladoa >= ladob + ladoc or ladob >= ladoa + ladoc:
                print("⚠ Error: Los lados no forman un triángulo válido.")

        anguloA = 0
        while anguloA <= 0:
            anguloA = pedir_numero("Ingrese el ángulo A: ")
            if anguloA <= 0:
                print("⚠ Error: El ángulo debe ser mayor que 0.")

        anguloB = 0
        while anguloB <= 0 or anguloA + anguloB >= 180:
            anguloB = pedir_numero("Ingrese el ángulo B: ")
            if anguloB <= 0 or anguloA + anguloB >= 180:
                print("⚠ Error: Los ángulos no forman un triángulo válido.")
   
    P = ladoa + ladob + ladoc
    S = (ladoa + ladob + ladoc) / 2
    A = (S * (S - ladoa) * (S - ladob) * (S - ladoc)) ** 0.5
    anguloC = 180 - (anguloA + anguloB)

    if opcion == 1:
        print(f"Semiperimetro del triángulo general: {S:.2f} {unidad_longitud}")
        print(f"Área del triángulo general: {A:.2f} {unidad_area}")
        resultados.append(
        f"Triangulo general -> ladoa={ladoa} {unidad_longitud}, ladob={ladob} {unidad_longitud}, ladoc={ladoc} {unidad_longitud}, "
        f"anguloA={anguloA:.2f}°, anguloB={anguloB:.2f}°, anguloC={anguloC:.2f}°, "
        f"semiperimetro={S:.2f} {unidad_longitud}, area={A:.2f} {unidad_area}"
    )
    elif opcion == 2:
        print(f"Perímetro del triángulo general: {P:.2f} {unidad_longitud}")
        resultados.append(
        f"Triangulo general -> ladoa={ladoa} {unidad_longitud}, ladob={ladob} {unidad_longitud}, ladoc={ladoc} {unidad_longitud}, "
        f"anguloA={anguloA:.2f}°, anguloB={anguloB:.2f}°, anguloC={anguloC:.2f}°, "
        f"perimetro={P:.2f} {unidad_longitud}"
    )
    elif opcion == 3:
        print(f"Perímetro del triángulo general: {P:.2f} {unidad_longitud}")
        print(f"Semiperimetro del triángulo general: {S:.2f} {unidad_longitud}")
        print(f"Área del triángulo general: {A:.2f} {unidad_area}")
        resultados.append(
        f"Triangulo general -> ladoa={ladoa} {unidad_longitud}, ladob={ladob} {unidad_longitud}, ladoc={ladoc} {unidad_longitud}, "
        f"anguloA={anguloA:.2f}°, anguloB={anguloB:.2f}°, anguloC={anguloC:.2f}°, "
        f"semiperimetro={S:.2f} {unidad_longitud}, area={A:.2f} {unidad_area}, perimetro={P:.2f} {unidad_longitud}"
    )

# 5. Triángulo rectángulo: hipotenusa,  área y perimetro

def triangulo_rectangulo():
    opcion = pedir_opcion_calculo(["Área", "Perímetro", "Ambos"])
                                   
    cateto_a = 0
    while cateto_a <= 0:
        cateto_a = pedir_numero("Ingrese el cateto a: ")
        if cateto_a <= 0:
            print("⚠ Error: El valor de los catetos no puede ser menor a 0.")

        cateto_b = 0
        while cateto_b <= 0:
            cateto_b = pedir_numero("Ingrese el cateto b: ")
            if cateto_b <= 0:
                print("⚠ Error: El valor de los catetos no puede ser menor a 0.")

        angulo_A = 0
        while not (0 < angulo_A < 90):
            angulo_A = pedir_numero("Ingrese el Angulo A: ")
            if not (0 < angulo_A < 90):
                print("⚠ Error: El angulo A debe ser mayor a 0 y menor a 90.")

    angulo_B = 90 - angulo_A
    angulo_C = 90

    cateto_c = (cateto_a ** 2 + cateto_b ** 2) ** 0.5
    Perimetro = cateto_a + cateto_b + cateto_c
    Area = (cateto_a * cateto_b) / 2

    print(f"Hipotenusa del triángulo rectángulo es: {cateto_c:2f} {unidad_longitud}")
    print(f"Ángulo A: {angulo_A:2F}°")
    print(f"Ángulo B: {angulo_B:2f}°")
    print(f"Ángulo C: {angulo_C:2f}°")

    if opcion == 1:
        print(f"Área del triángulo rectángulo es: {Area:.2f} {unidad_area}")
        resultados.append(
            f"Triangulo rectangulo -> catetoA={cateto_a} {unidad_longitud}, catetoB={cateto_b} {unidad_longitud}, hipotenusa={cateto_c:.2f} {unidad_longitud}, "
            f"anguloA={angulo_A:.2f}°, anguloB={angulo_B:.2f}°, anguloC={angulo_C:.2f}°, area={Area:.2f} {unidad_area}"
    )
    elif opcion == 2:
        print(f"Perímetro del triángulo rectángulo es: {Perimetro:.2f} {unidad_longitud}")
        resultados.append(
            f"Triangulo rectangulo -> catetoA={cateto_a} {unidad_longitud}, catetoB={cateto_b} {unidad_longitud}, hipotenusa={cateto_c:.2f} {unidad_longitud}, "
            f"anguloA={angulo_A:.2f}°, anguloB={angulo_B:.2f}°, anguloC={angulo_C:.2f}°, perimetro={Perimetro:.2f} {unidad_longitud}"
        )
    elif opcion == 3:
        print(f"Área del triángulo rectángulo es: {Area:.2f} {unidad_area}")
        print(f"Perímetro del triángulo rectángulo es: {Perimetro:.2f} {unidad_longitud}")
        resultados.append(
            f"Triangulo rectangulo -> catetoA={cateto_a} {unidad_longitud}, catetoB={cateto_b} {unidad_longitud}, hipotenusa={cateto_c:.2f} {unidad_longitud}, "
            f"anguloA={angulo_A:.2f}°, anguloB={angulo_B:.2f}°, anguloC={angulo_C:.2f}°, "
            f"area={Area:.2f} {unidad_area}, perimetro={Perimetro:.2f} {unidad_longitud}"
        )

    
# ══════════════════════════════════════════════════
#           FIGURAS 3D (SÓLIDOS)
# ══════════════════════════════════════════════════

# Funciones para calcular área, volumen y generatiz en figuras 3D
# 6. Esfera: área y volumen

def esfera():
    opcion = pedir_opcion_calculo(["Area", "Volumen", "Ambos"])

    r = -1
    while r <= 0:
        r = pedir_numero("Ingrese el radio de la esfera: ")
        if r <= 0:
            print("⚠ Error: El radio no puede ser menor o igual que 0.")

    A = 4 * PI * r ** 2                    
    V = (4 / 3) * PI * r ** 3 

    if opcion == 1:
        print(f"Área de la esfera es: {A:.2f} {unidad_area}")
        resultados.append(f"Esfera -> radio={r} {unidad_longitud}, area={A:.2f} {unidad_area}")
    elif opcion == 2:
        print(f"Volumen de la esfera es: {V:.2f} {unidad_volumen}")
        resultados.append(f"Esfera -> radio={r} {unidad_longitud}, volumen={V:.2f} {unidad_volumen}")
    elif opcion == 3:
        print(f"Área de la esfera es: {A:.2f} {unidad_area}")
        print(f"Volumen de la esfera es: {V:.2f} {unidad_volumen}")
        resultados.append(f"Esfera -> radio={r} {unidad_longitud}, area={A:.2f} {unidad_area}, volumen={V:.2f} {unidad_volumen}")

# 7. Cubo: área y volumen

def cubo():
    opcion = pedir_opcion_calculo(["Área", "Volumen", "Ambos"])
                                   
    l = -1
    while l <= 0:
        l = pedir_numero("Ingrese el lado del cubo: ")
        if l <= 0:
            print("⚠ Error: El lado no puede ser menor o igual que 0.")

    A = 6 * l ** 2
    V = l ** 3

    if opcion == 1:
        print(f"Área del cubo es: {A:.2f} {unidad_area}")
        resultados.append(f"Cubo -> lado={l} {unidad_longitud}, area={A:.2f} {unidad_area}")
    elif opcion == 2:
        print(f"Volumen del cubo es: {V:.2f} {unidad_volumen}")
        resultados.append(f"Cubo -> lado={l} {unidad_longitud}, volumen={V:.2f} {unidad_volumen}")
    elif opcion == 3:
        print(f"Área del cubo es: {A:.2f} {unidad_area}")
        print(f"Volumen del cubo es: {V:.2f} {unidad_volumen}")
        resultados.append(f"Cubo -> lado={l} {unidad_longitud}, area={A:.2f} {unidad_area}, volumen={V:.2f} {unidad_volumen}")
    
# 8. Cilindro: área y volumen

def cilindro():
    opcion = pedir_opcion_calculo(["Área", "Volumen", "Ambos"])
    r = -1
    while r <= 0:
        r = pedir_numero("Ingrese el radio del cilindro: ")
        if r <= 0:
            print("⚠ Error: El radio no puede ser menor o igual que 0.")

    h = -1
    while h <= 0:
        h = pedir_numero("Ingrese la altura del cilindro: ")
        if h <= 0:
            print("⚠ Error: La altura no puede ser menor o igual que 0.")

    A = 2 * PI * r * (r +h)
    V = PI * r ** 2 * h

    if opcion == 1:
        print(f"Área del cilindro es: {A:.2f} {unidad_area}")
        resultados.append(f"Cilindro -> radio={r} {unidad_longitud}, altura={h} {unidad_longitud}, area={A:.2f} {unidad_area}")
    elif opcion == 2:
        print(f"Volumen del cilindro es: {V:.2f} {unidad_volumen}")
        resultados.append(f"Cilindro -> radio={r} {unidad_longitud}, altura={h} {unidad_longitud}, volumen={V:.2f} {unidad_volumen}")
    elif opcion == 3:
        print(f"Área del cilindro es: {A:.2f} {unidad_area}")
        print(f"Volumen del cilindro es: {V:.2f} {unidad_volumen}")
        resultados.append(f"Cilindro -> radio={r} {unidad_longitud}, altura={h} {unidad_longitud}, area={A:.2f} {unidad_area}, volumen={V:.2f} {unidad_volumen}")


# 9. Cono: generatriz, área y volumen

def cono():
    opcion = pedir_opcion_calculo(["Área", "Volumen", "Generatriz", "Todos"])
                                   
    r = -1
    while r <= 0:
        r = pedir_numero("Ingrese el radio del cono: ")
        if r <= 0:
            print("⚠ Error: El radio no puede ser menor o igual que 0.")

    h = -1
    while h <= 0:
        h = pedir_numero("Ingrese la altura del cono: ")
        if h <= 0:
            print("⚠ Error: La altura no puede ser menor o igual que 0.")

        g = (r ** 2 + h ** 2) ** 0.5
    A = PI * r * (r + g)
    V = (1 / 3) * PI * r ** 2 * h

    if opcion == 1:
        print(f"Área del cono es: {A:.2f} {unidad_area}")
        resultados.append(f"Cono -> radio={r} {unidad_longitud}, altura={h} {unidad_longitud}, area={A:.2f} {unidad_area}")
    elif opcion == 2:
        print(f"Volumen del cono es: {V:.2f} {unidad_volumen}")
        resultados.append(f"Cono -> radio={r} {unidad_longitud}, altura={h} {unidad_longitud}, volumen={V:.2f} {unidad_volumen}")
    elif opcion == 3:
        print(f"Generatriz del cono es: {g:.2f} {unidad_longitud}")
        resultados.append(f"Cono -> radio={r} {unidad_longitud}, altura={h} {unidad_longitud}, generatriz={g:.2f} {unidad_longitud}")
    elif opcion == 4:
        print(f"Generatriz del cono es: {g:.2f} {unidad_longitud}")
        print(f"Área del cono es: {A:.2f} {unidad_area}")
        print(f"Volumen del cono es: {V:.2f} {unidad_volumen}")
        resultados.append(f"Cono -> radio={r} {unidad_longitud}, altura={h} {unidad_longitud}, generatriz={g:.2f} {unidad_longitud}, area={A:.2f} {unidad_area}, volumen={V:.2f} {unidad_volumen}")


# 10. Salir

def salir():

    print("\n════════════════════════════════════════════════════════════")
    print("                   RESUMEN DE LOS CÁLCULOS")
    print("════════════════════════════════════════════════════════════")

    if not resultados:
        print("No se realizaron cálculos.")
    else:

        print("-" * 60)
        print(f"{'Figura':<20} | {'Variable':<20} | {'Valor':<10}")
        print("-" * 60)


        for r in resultados:
            if "->" not in r:   # evita errores si el formato está mal
                continue

            datos = r.split("->")
            figura = datos[0].strip()
            variables = datos[1].split(",")

            for v in variables:
                if "=" in v:
                    nombre, valor = v.split("=")
                    print(f"{figura:<20} | {nombre.strip():<20} | {valor.strip():<10}")



    print("\nTodos los cálculos han finalizado.")
    print("Gracias por usar la calculadora.\n")

    exit()


def elegir_sistemas():

    global sistema, unidad_longitud, unidad_area, unidad_volumen

    print("""
╔══════════════════════════════════════════════════════════════════╗
║        CALCULADORA CIENTÍFICA — FIGURAS GEOMÉTRICAS              ║
╠══════════════════════════════════════════════════════════════════╣
║               Seleccione el sistema de medida                    ║
║                                                                  ║
║               1.  Metrico       2.  Imperial                     ║            
╚══════════════════════════════════════════════════════════════════╝""")
    

    try:
        opcion = int(input(" Elige una opcion: "))
    except ValueError:    
        print("⚠  Ingresa un número entero entre 1 o 2.")
        return elegir_sistemas()
    
    if opcion not in range (1, 3):
        print("⚠  Opción fuera de rango. Elige entre 1 o 2.")
        return elegir_sistemas()
    
    if opcion == 1:
        sistema = "metrico"
        unidad_longitud = "cm"
        unidad_area = "cm²"
        unidad_volumen = "cm³"
           
    else:
        sistema = "imperial"
        unidad_longitud = "in"
        unidad_area = "in²"
        unidad_volumen = "in³"
    
    menu()
    

def menu():

    print("""
╔══════════════════════════════════════════════════════════════════╗
║        CALCULADORA CIENTÍFICA — FIGURAS GEOMÉTRICAS              ║
╠══════════════════════════════════════════════════════════════════╣
║  FIGURAS 2D                         FIGURAS 3D                   ║
║   1. Circunferencia (radio→C, área)  6. Esfera                   ║
║   2. Trapecio                        7. Cubo                     ║
║   3. Rectángulo                      8. Cilindro                 ║
║   4. Triángulo general               9. Cono                     ║
║   5. Triángulo rectángulo            10. Salir                   ║   
╚══════════════════════════════════════════════════════════════════╝""")


    try:
        opcion = int(input("  Elige una opción (1–10): "))
    except ValueError:
        print("  ⚠  Ingresa un número entero entre 0 y 10.")
        return menu()

    if opcion not in range(0, 11):
        print("  ⚠  Opción fuera de rango. Elige entre 1 y 10.")
        return menu()

    resolver_figura(opcion)
    menu()

# ══════════════════════════════════════════════════
#                     MAIN
# ══════════════════════════════════════════════════

if __name__ == "__main__":
    elegir_sistemas()

1