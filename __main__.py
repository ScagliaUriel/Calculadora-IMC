from interfaces_usuario.consola_calculo_imc import main as calc_imc
from interfaces_usuario.consola_calculo_porcentaje_grasa import main as calc_pg
from interfaces_usuario.consola_calculo_calorias_reposo import main as calc_tmb
from interfaces_usuario.consola_calculo_calorias_actividad import main as calc_tmba
from interfaces_usuario.consola_calculo_calorias_adelgazar import main as calc_ca

def main():
    print("Calculadora de Indices Corporales\n")
    while True:
        try:
            opcion = int(input(
                "Seleccione un indice a calcular:\n"
                "1_ Índice de Masa Corporal(IMC).\n"
                "2_ Porcentaje de grasa.\n"
                "3_ Tasa Metabólica Basal(TMB).\n"
                "4_ Tasa Metabólica Basal según actividad.\n"
                "5_ Consumo recomendado de calorias para adelgazar.\n\n"
            ))
            if opcion == 1:
                calc_imc()
            elif opcion == 2:
                calc_pg()
            elif opcion == 3:
                calc_tmb()
            elif opcion == 4:
                calc_tmba()
            elif opcion == 5:
                calc_ca()
            else:
                print("Ingrese un número del 1 al 5.")
                continue
            salir = input("Presione enter para volver al menú principal, para salir oprima 0: \n")
            if salir == "0":
                break
        except ValueError:
            print("Por favor, ingrese solo números validos.")
            
if __name__ == "__main__":
    main()