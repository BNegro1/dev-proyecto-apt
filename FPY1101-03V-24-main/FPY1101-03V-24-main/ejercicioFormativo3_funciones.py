import random as rd,csv
#import csv 

CARGOS = ['ceo','desarrollador','analista de datos']

#función registrar trabajador
def registrar_trabajador(trabajadores):
    nombre = input("Ingrese nombre y apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador (CEO/Desarrollador/Analista de datos): ").lower()
    while cargo not in CARGOS:
        print("Cargo no válido, por favor intenta nuevamente")
        cargo = input("Ingrese el cargo del trabajador (CEO/Desarrollador/Analista de datos): ").lower()
    #sueldoBruto = int(input("Ingrese sueldo Bruto: "))
    sueldoBruto = rd.randint(1000,5000)

    #calculo de los valores de afp y de salud.
    descSalud = sueldoBruto * 0.07
    descAFP = sueldoBruto * 0.12
    liquidoPago = sueldoBruto - descSalud - descAFP

    trabajadores.append({
        'Nombre' : nombre,
        'Cargo' : cargo,
        'SueldoBruto' : sueldoBruto,
        'DescSalud' : descSalud,
        'DescAFP' : descAFP,
        'LiquidoPago' : liquidoPago
    })


# función listar trabajadores
def listar_trabajadores(trabajadores):
    print("Lista de Trabajadores")
    for trabajador in trabajadores:
        print(trabajador)


#función imprimir planillas de sueldo
def imprimir_planilla(trabajadores):
    cargoSeleccionado = input("Ingrese el cargo para imprimir la planilla (o presiona ENTER para imprimir todos) : ")
    if cargoSeleccionado == "":
        trabajadores_a_imprimir = trabajadores
        nombreArchivo = 'planilla_todos.txt'
    elif cargoSeleccionado in CARGOS:
        trabajadores_a_imprimir = []
        for trabajador in trabajadores:
            if trabajador['Cargo'] == cargoSeleccionado:
                trabajadores_a_imprimir.append(trabajador)
        nombreArchivo = f'planilla_{cargoSeleccionado}.txt'
    else:
        print("Cargo Inválido")
        return
    
    with open(nombreArchivo,'w') as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"Nombre y Apellido: {trabajador['Nombre']}\n")
            archivo.write(f"Cargo: {trabajador['Cargo']}\n")
            archivo.write(f"Sueldo Bruto: ${trabajador['SueldoBruto']}\n")
            archivo.write(f"Desc Salud : ${trabajador['DescSalud']}\n")
            archivo.write(f"Desc AFP : ${trabajador['DescAFP']}\n")
            archivo.write(f"Liquido a Pago : ${trabajador['LiquidoPago']}\n\n")

def imprimir_csv(trabajadores):

    nombreArchivo = 'archivocsv.csv'

    encabezado = ['Nombre','Cargo','SueldoBruto','DescSalud','DescAFP','LiquidoPago']

    with open(nombreArchivo,'w') as archivo_csv:
        #escritor = csv.writer(archivo_csv)
        escritor = csv.DictWriter(archivo_csv,fieldnames=encabezado)

        #escritor.writerow(encabezado)
        escritor.writeheader()
        #escritor.writerows(trabajadores)

        for dato in trabajadores:
            escritor.writerow(dato)




    