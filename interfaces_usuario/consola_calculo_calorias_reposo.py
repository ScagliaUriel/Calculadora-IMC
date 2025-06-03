from calculadora_indices.funciones import calcular_calorias_en_reposo as calc_reposo, obtener_genero_tmb as val_gen

def main():
    try:
        print ("Calculadora de Tasa Metabólica Basal\n")
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        edad = int(input("Ingrese su edad: "))
        valor_genero, _= val_gen()
        tmb = calc_reposo(peso, altura, edad, valor_genero)
        print(f"\nTu Tasa Metabólica Basal(TMB) es {tmb:.2f} calorías por día.\n")
    except ValueError:
        print("Por favor, ingrese solo números validos.")

if __name__ == "__main__":
    main()