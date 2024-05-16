# Descuento en medicinas
# Debemos cargar por teclado precio de mediamento
# todos todos los medicamentos tienen un descuento del 35%
# mostrar precio actual
# mostar monto del decuento
# mostrar monto final

precio_medicamento = float(input("Ingrese el monto a pagar por el medicamento: "))
monto_descuento = precio_medicamento * 0.35
monto_final = precio_medicamento - monto_descuento

print(f"Precio actual: {precio_medicamento}\nMonto descuento: {monto_descuento}\nMonto final: {monto_final}")