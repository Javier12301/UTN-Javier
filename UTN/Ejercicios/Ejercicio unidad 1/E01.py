# División con Resto
#Plantear un script (directamente en el shell de Python)
# que permita informar, para dos valores a y b el resultado de la división a/b
# y el resto de esa divisón.

a = int(input("Ingrese el numerador: "))
b = int(input("Ingrese el denominador: "))

resultado = a/b
print(f"El resultado de la división entre {a}/{b} es {resultado} y el resto de la división es: {a%b}")

