# Secuenca de impares
"""
    cargar dos números, e imprimir numeros impares que esten comprendido entre ellos
    de forma ascendente y descendente
"""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

lista_numero1 = []
lista_numero2 = []

if numero1 > numero2:
    mayor, menor = numero1, numero2
else:
    mayor, menor = numero2, numero1

# Debemos crear una secuencia ascendente
# Este debe ir de [men, mayor

if menor % 2 == 0:
    menor += 1
if mayor % 2 == 0:
    mayor -= 1

print(mayor)
print(menor)
#[5,9]

print("Secuencia ascendente")
ascend = range(menor, mayor + 2, 2)
for num in ascend:
    print(num, end = ' | ')

print("\nSecuencia descendente")
descend = range(mayor, menor - 2, -2)
for num in descend:
    print(num, end = ' | ')