# Ventas por sucursal
# debemos ingresar una serie de numeros que representan "CANTIDAD VENTAS"
# que se eralizan en las diferentes sucursales del pais de una empresa

"""
Requerimientos:
    a) Informar cantidad de ventas ingresadas
    b) total ventas
    c) cantidad ventas cuyo valor este enter 100 y 300 unidades
    d) cantidad ventas con 400, 500 y 600 unidadse
    e) indicar si hubo cantidad de ventas inferior a 50
"""


ventas_realizadas = 0
cont_vent1 = 0
cont_vent400 = 0
cont_vent500 = 0
cont_vent600 = 0
ventas_inferior50 = False
total_ventas = 0
cantidad_ventas = int(input("Ingrese la cantidad de ventas: "))
while cantidad_ventas >= 0:
    ventas_realizadas += 1
    # 100 <= cant_ventas <= 300
    total_ventas += cantidad_ventas
    if cantidad_ventas >= 100 and cantidad_ventas <= 300:
        cont_vent1 += 1
    if cantidad_ventas == 400:
        cont_vent400 += 1
    if cantidad_ventas == 500:
        cont_vent500 += 1
    if cantidad_ventas == 600:
        cont_vent600 += 1
    if cantidad_ventas < 50:
        ventas_inferior50 = True
    cantidad_ventas = int(input("Ingrese la cantidad de ventas (cantidades negativas terminan el programa): "))

print(f"Se ingreso una cantidad de ventas de : {ventas_realizadas}")
print(f"Total: {ventas_realizadas}")
print(f"Cantidad de ventas entre 100 y 300: {cont_vent1}")
print(f"Cantidad de ventas entre 400: {cont_vent400}")
print(f"Cantidad de ventas entre 500: {cont_vent500}")
print(f"Cantidad de ventas entre 600: {cont_vent600}")
if ventas_inferior50:
    print("Hubo ventas inferior a 50 unidades")
else:
    print("No hubo ventas inferior a 50 unidades")