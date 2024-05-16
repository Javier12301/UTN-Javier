# mayor y menor
"""
Desarrollar un programa que genere 8 numeros aleatorios entre 1 y 100
deebmos establecer cual fue el mayor de los pares y el menor de los impares
en el conjunto

ejemplo, una secuencia de 8,15,9,2,27,18,6,33; el mayor de los pares es el 18 y
el menor de los impares el numero 9
"""
import random
mayor = None
menor = None

for i in range(8):
    numero = random.randint(1, 100)
    print(numero, end=' | ')
    if numero % 2 == 0:
        if mayor is None or numero > mayor:
            # sabemos que es par, entonces solo verificamos que sea mayor
            mayor = numero
    else:
        if menor is None or numero < menor:
            menor = numero

print(f"\nEl mayor de los pares es: {mayor}")
print(f"\nEl menor de los impares es: {menor}")

