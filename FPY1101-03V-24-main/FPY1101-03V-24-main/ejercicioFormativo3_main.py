import ejercicioFormativo3_funciones as fn

trabajadores=[]

while True:
    print("Bienvenidos al sistema de sueldo")
    print("1. Registrar Trabajadores")
    print("2. Listar Trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir")
    opcion = int(input("Seleccion su opción: "))

    if opcion == 1 :
        fn.registrar_trabajador(trabajadores)
    elif opcion == 2:
        fn.listar_trabajadores(trabajadores)
    elif opcion == 3:
        fn.imprimir_planilla(trabajadores)
        print("¡¡¡¡¡¡¡PLANILLA GENERADA!!!!!!")
    elif opcion == 4:
        fn.imprimir_csv(trabajadores)
        print("Impresion csv con exito!")
        break
    else:
        print("Opción no válida, intente nuevamente")

