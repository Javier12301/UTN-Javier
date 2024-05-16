# Cuadrado de cubos
# Leer dos números y calcular:
 # Suma de sus cuadrados
 # Promedio de sus cubos

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

# SUma de sus cuadrados
 # 1. hacerlo directo a^2 + b^2
r_sumacuadrados = a**2 + b**2

# promedio de sus cubos
r_promedio = (a**3 + b**3)/2

print(f"Suma cuadrados: {r_sumacuadrados}\nPromedio de sus cubos: {r_promedio}")
