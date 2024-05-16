# Discriminante
"""
    cargar serie de números
    que representan discriminantes
    de diferentes ecuaciones de segundo grado
    finaliza cuando el matematico no desea seguir cargando

    requerimientos:
    1. cantidad de discriminantes que dan 2 raices
    2. cantidad de discriminantse que dan una unica raiz
    3. cantidad discriminante que dan raices en el campo imaginario
    4. indicar porcentaje que representa punto c sobre total de discriminantes
    (cont_imaginario * 100) / (cont_total)
"""

cont_total = 0
cont_2raiz = 0
cont_1raiz = 0
cont_imaginario = 0

continuar = 1
while continuar != 0:
    valor_discriminante = int(input("Ingrese el valor del discriminante: "))
    cont_total += 1
    if valor_discriminante > 0:
        cont_2raiz += 1
    elif valor_discriminante == 0:
        cont_1raiz += 1
    else:
        cont_imaginario += 1
    opcion = input("¿Desea continuar (S/N)?\nIngrese una opción: ")
    if opcion.upper() == "N":
        continuar = 0
        print("Muchas gracias por usar el programa para calcular determinante...")

# Salida
print(f"Discriminantes que dan 2 raíces: {cont_2raiz}")
print(f"Discriminantes que dan 1 raíz: {cont_1raiz}")
print(f"Discriminantes que dan imaginario: {cont_imaginario}")

porcentaje = (cont_imaginario * 100) / cont_total
print(f"El porcentaje del conteo de los imaginario con respecto del total es de: {round(porcentaje, 2)}")
