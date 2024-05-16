# Complejo de cines
"""
Requerimientos:
    1. Por cada función, se conoce "espectadores" y "descuentos (S/N)"
    2. La carga termina cuando la cantidad de espectadores sea igual a 0

    funcionalidades:
    a. calcular la recaudación total, considerando que el valor de entrada es de 50$ en días
    con descuento y 75$ sin descuento

    b. determinar cuantas funciones con descuento se efectuaron y que porcentaje representan
    sobre el total de funciones
"""

print("COMPLEJO DE CINES")
print("-"*80)

# inicializar contadores y acumuladores
monto = 0 # recaudación total
funciones = 0
funciones_dto = 0

espectadores = int(input("Ingrese la cantidad de espectadores: "))

while espectadores != 0:
    continuar_loop = 1
    while continuar_loop != 0:
        descuento = input("Descuento (S/N): ")
        if descuento == "S":
            funciones_dto += 1
            precio = 50
            continuar_loop = 0
        elif descuento == "N":
            precio = 75
            continuar_loop = 0
        else:
            print("Error, ingrese \"S\" si es que se aplico o \"N\" si no se aplico.")
    monto += (espectadores * precio)
    funciones += 1
    espectadores = int(input("Ingrese la cantidad de espectadores (0 termina con el programa): "))

# Salida
print(f"La recaudación total es de: {monto}$")
if funciones != 0:
    porcentaje = (funciones_dto * 100) / funciones
else:
    porc = 0
print(f"Se realizo {porcentaje}%")