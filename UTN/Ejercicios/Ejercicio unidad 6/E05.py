# busqueda mayor
"""
Realizar un programa que permita buscar
el mayor de 10.000 números aleatorios generados en el rango de
[-100.000, 100.000]. Además de informar el mayor,
debe informar el porcentaje que representan
los números positivos sobre el total de números generados.
"""
import random

cantidad_valores = 10000 # tenemos que buscar el mayor de 10.000 números
mayor = None # no se conoce un mayor
contador_positivo = 0
i = 0 # numeros ya generados

while i < cantidad_valores:
    n = random.randint(-100000,100000)
    if mayor is None or n > mayor:
        mayor = n
    # verificar si el mayor es positivo y contabilizar
    if n > 0:
        contador_positivo += 1
    i+= 1

print(f"El mayor de 10 mil números probado es: {mayor}")
porcentaje = (contador_positivo * 100) / i
print(f"Porcentaje: {str(round(porcentaje,2))} %")
