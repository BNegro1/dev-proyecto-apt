import funciones as fn

trabajadores = []

while True:
    print("Bienvenidos al super sistema de Pago de Sueldos")
    print("1. Registrar trabajador")
    print("2. Listar los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir")

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        fn.registrar_trabajador(trabajadores)
    elif opcion == 2:
        fn.listar_trabajadores(trabajadores)
    elif opcion == 3:
        fn.imprimir_plantilla(trabajadores)
    elif opcion == 4:
        fn.imprimir_csv(trabajadores)
        print("CSV creado!!")
        break
    else:
        print("Opción no válida, seleccione nuevamente")
