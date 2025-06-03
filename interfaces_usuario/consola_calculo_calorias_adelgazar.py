from calculadora_indices.funciones import consumo_calorias_recomendado_para_adelgazar as calc_adelgazar, obtener_genero_tmb as val_gen

def main():
    print ("Calculadora de consumo de calorias recomendado para adelgazar\n")
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        edad = int(input("Ingrese su edad: "))
        valor_genero, _ = val_gen()
        resultado = calc_adelgazar(peso, altura, edad, valor_genero)
        print(resultado)
    except ValueError:
        print("Por favor, ingrese solo números validos.")
        
if __name__ == "__main__":
    main()