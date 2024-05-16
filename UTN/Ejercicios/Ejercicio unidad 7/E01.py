"""
    Tenemos n competidores (debemos ingresarlos por teclado)
    el programa debe cargar, por cada competido, nombre y tiempo de carrera

    Requerimiento:
    a. determinar y mostrar el nombre del ganador de la carrera
    b. ingresar por teclado tiempo record registrado para dicha carrera, si el tiempo del
    ganador es menor al tiempo record, mostrar mensaje
    c. calcular y mostrar tiempo promedio entre todos los ciclistas
"""

competidores = int(input("Ingrese el número de competidores: "))
cont = 0
acum = 0
ganador = None

for i in range(competidores):
    print("Ciclista",i)
    nombre = input("Ingrese nombre: ")
    tiempo = int(input("Ingrese tiempo del competidor: "))
    if ganador is None or tiempo < ganador[1]:
        ganador = nombre, tiempo
    cont += 1
    acum += tiempo # para calcular tiempo promedio

if competidores > 0:
    record = int(input("Ingrese record actual: "))
    print("El ganador es", ganador[0])
    if ganador[1] < record:
        print("El ganador supero el record")
    # calcular promedio
    if cont > 0:
        promedio = (acum * 100) / cont
    else:
        promedio = 0
    print("Tiempo promedio general: ", promedio)
else:
    print("No se ingresaron competidores")









