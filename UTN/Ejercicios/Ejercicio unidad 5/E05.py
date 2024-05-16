# Menu opciones básico
"""
Opciones:
    1. mostrar superficie de un triangulo usando fórmula de herón
    Superficie = sqrt(s(s-a)(s-b)(s-c))
    donde s = (a+b+c)/2

    2. Perimetro del triangulo

    3. Longitud del lado menor

    4. Si la opción no fue ni 1,2 o 3 informar un error
"""

print("Menu de opciones básicos")
opcion = int(input("\n1. Superficie de un triangulo (Fórmula de Herón)\n2. Perímetro del triángulo\n3. Longitud del lado menor.\nIngrese la opción: "))
a = int(input("Ingresar lado a: "))
b = int(input("Ingresar lado b: "))
c = int(input("Ingresar lado c: "))
if opcion == 1:
    # Calcular semi perimetro
    s = (a+b+c) / 2
    # Calcular superficie
    superficie = pow(s*(s-a)*(s-b)*(s-c),0.5)
    print(f"La superficie es: {superficie}")
elif opcion == 2:
    perimetro = a + b + c
    print(f"El perimetro del triangulo es: {perimetro}")
elif opcion == 3:
    if a < b and a < c:
        menor = a
    elif b < a and b < c:
        menor = b
    else:
        menor = c
    print(f"La longitud del menor de los lados es: {menor}")
else:
    print("No existe la opción ingesada.")