from calculadora_indices.funciones import calcular_calorias_en_actividad as calc_actividad, obtener_genero_tmb as val_gen, obtener_actividad

def main():
    print("Calculadora de Tasa Metabólica Basal según actividad física\n")
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        edad = int(input("Ingrese su edad: "))
        valor_genero, _= val_gen()
        valor_actividad = obtener_actividad() 
        tmb_actividad = calc_actividad(peso, altura, edad, valor_genero, valor_actividad)
        print(f"\nTu Tasa Metabólica Basal en actividad es {tmb_actividad:.2f}\n")
    except ValueError:
        print("Por favor, ingrese solo números validos.")
        
if __name__ == "__main__":
    main()