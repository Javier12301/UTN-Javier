"""
    Desarrollar un programa que implemente el calculo de la sucesión:
    f(n) = n/2 , SI n es par
    f(n) = 3n + 1, SI n es impar
"""
import os


def sum_collatz(n):
    sucesion = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        # insertar n en la lista
        # Truncar
        n = int(n)
        sucesion.append(n)
    return sucesion

def resultados(sucesion, long_orbita, prom_orbita, mayor_orbita):
    # Imprimir número de orbita
    print(f"Orbita de n = {sucesion[0]}")
    # Imprimir sucesión
    print(sucesion)
    # Imprimir longitud
    print(f"Longitud de órbita: {long_orbita}")
    # Promedio
    print(f"Promedio de todos los valores de la órbita: {prom_orbita}")
    # Mayor
    print(f"Mayor de los números en la órbita: {mayor_orbita}")
def clear_terminal():
    print("\033[H\033[2J")

while True:
    n = int(input("Ingrese el valor n: "))
    sucesion = sum_collatz(n)
    # Obtener suma de la sucesion
    suma_orbita = sum(sucesion)
    # Obtener longitud
    longitud_orbita = len(sucesion)
    # Promedio
    promedio_orbita = round(suma_orbita / longitud_orbita, 1)
    # Mayor de los números
    mayor_orbita = max(sucesion)
    # Resultados
    resultados(sucesion, longitud_orbita, promedio_orbita, mayor_orbita)
    user_input = input("¿Desea continuar? (S/N): ")
    print("\n")
    if user_input.lower() == "n":
        break









