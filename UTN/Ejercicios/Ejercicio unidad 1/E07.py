# Precio del boleto
"""Se desea conocer el precio de un
boleto de viaje en
ómnibus de media distancia. Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre), más un valor extra calculado en base a la cantidad de kilómetros a recorrer:  Por cada kilómetro a recorrer
se cobra $0.30 de adicional."""

# Constante
adicionalpor_km = 0.30

# Carga de datos
monto_base = float(input("Ingrese el monto base: "))
kma_recorrer = float(input("Ingrese los km que va a recorrer: "))

# Proceso
adicional_total = kma_recorrer * adicionalpor_km
costo_total = monto_base + adicional_total
print("El costo total del boleto es de: ",costo_total)