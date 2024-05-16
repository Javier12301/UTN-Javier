"""1. Operaciones de orden con 3 nros.
Realizar un programa que tome tres números,
 los ordene de mayor a menor.
Sobre los valores ordenados diga si el tercero es el resto de la división de los dos primeros. """

# tomamos tres numeros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

num_mayor = 0
num_intermedio = 0
num_menor = 0

if num1 > num2 and num1 > num3:
    num_mayor = num1
    if num2 > num3:
        num_intermedio = num2
        num_menor = num3
    else:
        num_intermedio = num3
        num_menor = num2
elif num2 > num1 and num2 > num3:
    num_mayor = num2
    if num1 > num3:
        num_intermedio = num1
        num_menor = num3
    else:
        num_intermedio = num3
        num_menor = num1
else:
    num_mayor = num3
    if num1 > num2:
        num_intermedio = num1
        num_menor = num2
    else:
        num_intermedio = num2
        num_menor = num1

print(f"Número sin ordenar: ({num1}, {num2}, {num3})")
print(f"Número ordenados: ({num_mayor}, {num_intermedio}, {num_menor})")

# comprobar si el tercero es el resto de la división de los dos primeros
if (num_mayor % num_intermedio) == num_menor:
    print("Es el resto de los dos primeros")
else:
    print("No es el resto de los dos primeros")