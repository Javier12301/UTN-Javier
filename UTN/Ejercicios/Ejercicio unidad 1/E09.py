# Area de un rectangulo
"""Desarrollar un programa que, conociendo el valor del perímetro de un rectángulo y el valor de uno de los lados de ese rectángulo, calcule y muestre el valor del área (o superficie) de ese rectángulo."""
#Perimetro = 2(A + B)
#Area = b*a

lado_a = int(input("Ingrese lado a: "))
perimetro = float(input("Ingrese perimetro: "))
lado_b = (perimetro - (2*lado_a))/2

# obtenemos el area
Area = lado_b * lado_a

print("El area del rectangulo es de: ",Area)