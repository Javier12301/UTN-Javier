# Cuadrado de un binomio

a = int(input("Ingrese el valor para el término a: "))
b = int(input("Ingrese el valor para el término b: "))


resSinPropiedad = (a + b) * (a + b)
resConPropiedad = (a**2 + 2*a*b + b**2)


print(f"Calculando de forma directa: {resSinPropiedad}")
print(f"Calculando por desarollo del cuadrado: {resConPropiedad}")