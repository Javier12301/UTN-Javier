import random

random.seed(20220512)
total_numeros = 25000

# req 1
cont_multiplo3 = 0
cont_multiplo5 = 0
cont_ninguno_anteriores = 0

# req 2
mayor = None

# req3
total_pares = 0
cont_pares = 0


for i in range(total_numeros):
    numeros = random.randint(1,45000)
    #req 1
    if numeros % 3 == 0:
        cont_multiplo3 += 1
    elif numeros % 5 == 0:
        cont_multiplo5 += 1
    else:
        cont_ninguno_anteriores += 1
    # req 2
    primer_digito = numeros
    while primer_digito >= 10:
        primer_digito //= 10
    if primer_digito == 1:
        if mayor is None or numeros > mayor:
            mayor = numeros
    # req 3
    if numeros % 2 == 0 and numeros % 11 == 0:
        total_pares += numeros
        cont_pares += 1

# Salida
#1
print(cont_multiplo3)
print(cont_multiplo5)
print(cont_ninguno_anteriores)

# 2
print(mayor)

#3
if cont_pares != 0:
    promedio_3 = total_pares // cont_pares
else:
    promedio_3 = 0
print(promedio_3)

# 4
porcentaje_4_multiplo3 = ((cont_multiplo3) * 100) // total_numeros
porcentaje_4_multiplo5 = ((cont_multiplo5) * 100) // total_numeros
porcentaje_4_ninguno_anteriores = ((cont_ninguno_anteriores) * 100) // total_numeros

print(f"{porcentaje_4_multiplo3};{porcentaje_4_multiplo5};{porcentaje_4_ninguno_anteriores}")