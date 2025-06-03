from calculadora_indices.funciones import calcular_porcentaje_grasa as calc_grasa, clasificar_pg, obtener_genero_pg as val_gen

def main():
    try:
        print("Calculadora de porcentaje de grasa corporal\n")
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        edad = int(input("Ingrese su edad: "))
        valor_genero, genero_letra = val_gen()
        porcentaje_grasa = calc_grasa(peso, altura, edad, valor_genero)
        clasificacion = clasificar_pg(porcentaje_grasa, edad, genero_letra)
        print(f"\nTu porcentaje de grasa corporal es de {porcentaje_grasa:.2f}%\n")
        print(f"{clasificacion}\n")
    except ValueError:
        print("Por favor, ingrese solo números validos.")
    
if __name__ == "__main__":
    main()