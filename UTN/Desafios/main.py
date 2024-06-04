__author__ = 'Catedra de AED'


# pasó la primera venta del vendedor 2?
aviso = False

# si no se cargan ventas del vendedor 2, menor_importe queda en None...
menor_importe = None

# acumuladores de cantidades...
c1 = c2 = 0

# acumuladores de importes...
i1 = i2 = 0

print('Ventas de un Comercio... ingrese los datos de cada venta...')

# ingresar datos de la primera venta...
codigo = -1
while codigo < 0 or codigo > 2:
    codigo = int(input('Codigo de vendedor (1 o 2) (0 para cortar): '))
    if codigo > 2 or codigo < 0:
        print('Error... se pidio 1 o 2 o 0 para cortar...')

cantidad = int(input('Cantidad vendida: '))
importe = float(input('Importe: '))

menor_importe = importe

while codigo != 0:
    if codigo == 1:
        c1 += cantidad
        i1 += importe

    elif codigo == 2:
        c2 += cantidad
        i2 += importe

        # Aplicar mecanismo de cálculo del menor...
        if importe < menor_importe:
            menor_importe = importe

    # ingresar el siguiente codigo y volver al ciclo...
    codigo = -1
    while codigo < 0 or codigo > 2:
        codigo = int(input('Codigo de vendedor (1 o 2) (0 para cortar): '))
        if codigo > 2 or codigo < 0:
            print('Error... se pidio 1 o 2 o 0 para cortar...')

    cantidad = int(input('Cantidad vendida: '))
    importe = float(input('Importe: '))

# Calcular el importe promedio...
promedio = (i1 + i2) / 2

print('Cantidad de productos vendida por el vendedor 1:', c1)
print('Cantidad de productos vendida por el vendedor 2:', c2)
print('Importe total facturado por el vendedor 1:', i1)
print('Importe total facturado por el vendedor 2:', i2)
print('Importe de la menor venta del vendedor 2:', menor_importe)
print('Importe promedio entre los dos vendedores:', promedio)