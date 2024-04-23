# Desarrollar un programa que, conociendo el valor del área (o superficie) de un cuadrado, obtenga y muestre el valor del perímetro de ese cuadrado.

Area = int(input("Ingrese el área del cuadrado: "))

# proceso
Lado = Area**(1/2)
#También puede ser Lado = pow(Area, 0.5)


Perimetro = 4 * Lado

print("El perimetro es de: ",Perimetro)