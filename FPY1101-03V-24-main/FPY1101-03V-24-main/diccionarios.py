mi_diccionario = {}

mi_diccionario = {"clave1":"valor1",
                  "clave2":"valor2"
                  }

print(mi_diccionario["clave1"])
print(mi_diccionario)

#ejemplo
estudiante={
    "nombre" : "Juanito",
    "edad" : 15,

    "carrera" : "Ingenieria" 
}

print(estudiante)
print(estudiante["nombre"])

estudiante["promedio"] = 3.9 # agregando key
estudiante["nombre"] = "Maria"
estudiante["edad"] = 18

print(estudiante)

for clave,valor in estudiante.items():
    print(clave,":",valor)




