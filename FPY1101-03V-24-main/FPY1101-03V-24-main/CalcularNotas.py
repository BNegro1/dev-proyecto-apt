# calcular promedio de 3 notas
# nota 1 30%
# nota 2 30%
# nota 3 40%

# Promedio equivale al 60 % de la nota final
# examen equivale al 40% de l anota final
# calcule nota final de la asignatura

nota1 = float(input("Ingrese nota 1: ")) # decimales
nota2 = float(input("Ingrese nota 2: ")) # decimales
nota3 = float(input("Ingrese nota 3: ")) # decimales

promNotas = nota1*0.3+nota2*0.3+nota3*40/100

notaExamen = float(input("Ingrese nota examen: "))

#examen = notaExamen * 0.4

promFinal = promNotas*0.6 + notaExamen*0.4

print("Su promedio final es: ",promFinal)


# condiciones --SI --> IF

if promFinal >= 40:
    print("Esta aprobado")
else:
    print("Esta reprobado")

    
