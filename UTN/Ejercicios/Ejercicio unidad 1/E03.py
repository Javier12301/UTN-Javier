# Área de un Triángulo
# Ecuación A = (b*h)/2 -> b = base , h = altura

''' Ejercicio
Desarrolle un programa para calcular el área de un triángulo,
cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base.
(Observar que la altura no es un dato... sólo se indica la forma de calcularla de acuerdo a la base que sí es un dato).
'''

triangulo_base = float(input("Ingresar valor de la base del triángulo: "))
triangulo_altura = triangulo_base ** 2
triangulo_area = (triangulo_base*triangulo_altura)/2

print(f"El área del triangulo es: {triangulo_area}")

