#Calculadora de indice de masa corporal.
def calcular_IMC(peso, altura):
    imc= peso / (altura ** 2)
    return imc

#Calculadora de porcentaje de grasa corporal.
def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    porcentaje_grasa = (1.2 * calcular_IMC(peso, altura)) + (0.23 * edad) - 5.4 - valor_genero
    return porcentaje_grasa

#Calculadora de calorias en reposo.
def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    altura = altura * 100
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return tmb

#Calculadora de calorias en actividad fisica.
def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    tmb_actividad_fisica = tmb * valor_actividad
    return tmb_actividad_fisica

#Calculadora de consumo de calorias recomendado para adelgazar.
def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rcd_inf = float(tmb * 0.80)
    rcd_sup = float(tmb * 0.85)
    return f"\nPara adelgazar es recomendado que consumas entre: {rcd_inf:.2f} y {rcd_sup:.2f} calorias al día\n"

#Clasificador de IMC.
def clasificar_IMC(imc):
    if imc < 16:
        return "Delgadez severa"
    elif 16 <= imc < 17:
        return "Delgadez moderada"
    elif 17 <= imc < 18.5:
        return "Delgadez aceptable"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad tipo I"
    elif 35 <= imc < 40:
        return "Obesidad tipo II"
    elif 40 <= imc < 50:
        return "Obesidad tipo III o mórbida"
    else:
        return "Obesidad tipo IV o extrema"

#Clasificar el porcentaje de grasa
def clasificar_pg(porcentaje_grasa, edad, valor_genero):
    rangos = {
        (20, 29): {'M': (11, 20), 'F': (16, 28)},
        (30, 39): {'M': (12, 21), 'F': (17, 29)},
        (40, 49): {'M': (14, 23), 'F': (18, 30)},
        (50, 59): {'M': (15, 24), 'F': (19, 31)},
    }

    for rango_edad, valores in rangos.items():
        if rango_edad[0] <= edad <= rango_edad[1]:
            min_val, max_val = valores[valor_genero]
            if min_val <= porcentaje_grasa <= max_val:
                return f"Porcentaje dentro del rango normal ({min_val}% - {max_val}%)"
            else:
                return f"Porcentaje fuera del rango recomendado ({min_val}% - {max_val}%)"
    return "Edad fuera de los rangos establecidos para la clasificación."   

#Funciones para obtener el genero.
def obtener_genero_tmb():
    while True:
        try:
            genero = int(input("Ingrese su género (Hombre: 1 / Mujer: 2): "))
            if genero == 1:
                return 5, "M"
            elif genero == 2:
                return -161, "F"
            else:
                print("Ingrese el número 1 o 2.")
        except ValueError:
            print("Por favor, ingrese solo números validos.")

def obtener_genero_pg():
    while True:
        try:
            genero = int(input("Ingrese su género (Hombre: 1 / Mujer: 2): "))
            if genero == 1:
                return 10.8, "M"
            elif genero == 2:
                return 0, "F"
            else:
                print("Ingrese el número 1 o 2.")
        except ValueError:
            print("Por favor, ingrese solo números válidos.")

#Obtener la actividad semanal
def obtener_actividad():
    while True:
        try:
            opcion = int(input(
                "\nSeleccione una opción dependiendo de su actividad física semanal:\n"
                "1_ Poco o nada de ejercicio.\n"
                "2_ Ejercicio ligero (1 a 3 días a la semana)\n"
                "3_ Ejercicio moderado (3 a 5 días a la semana)\n"
                "4_ Deportista (6 - 7 días a la semana)\n"
                "5_ Atleta (entrenamientos mañana y tarde).\n"
            ))
            valores = {
                1: 1.2,
                2: 1.375,
                3: 1.55,
                4: 1.725,
                5: 1.9
            }
            if opcion in valores:
                return valores[opcion]
            else:
                print("Ingrese un número entre 1 y 5.")
        except ValueError:
            print("Por favor, ingrese solo números válidos.")