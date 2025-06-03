from calculadora_indices.funciones import calcular_IMC, clasificar_IMC

def main():
    try:
        print ("Calculadora de indice de masa corporal(IMC)\n")
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        imc = calcular_IMC(peso, altura)
        clasif = clasificar_IMC(imc)
        print(f"\nTu IMC es {imc:.2f} y tu clasificación es {clasif}.\n") 
    except ValueError:
        print("Por favor, ingrese solo números validos.")
        
if __name__ == "__main__": 
    main()