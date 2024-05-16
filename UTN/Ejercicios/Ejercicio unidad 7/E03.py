# ssueldo y aguinaldo
"""
 Ingresar por teclado sueldos de un vendedor

    Determinar:
     a. calcular aguinaldo, sabiendo que es la mitad del sueldo más alto del periodo
     b. determinar que mes recibio el sueldo más bajo del periodo
     c. informar sueldo promedio del semestre
"""

total = 0
primero = True
semestre = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio")
for mes in semestre:
    sueldo = float(input(f"Ingrese sueldo de {mes}: "))
    if primero == True:
        mayor = sueldo
        menor = sueldo, mes
        primero = False
    else:
        if sueldo > mayor:
            mayor = sueldo
        if sueldo < menor[0]:
            menor = sueldo, mes
    total += sueldo

# aguinaldo
aguinaldo = mayor / 2
print(f"El aguinaldo es de: {aguinaldo}")
# mes que recibio sueldo más bajo
print(f"El mes que se recibió el sueldo más bajo es {menor[1]}, se recibio un sueldo de: {menor[0]}")
# sueldo promedio
promedio = total / 6
print(f"El promedio del semestre es de: {round(promedio, 2)}$")