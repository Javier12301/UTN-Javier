# Turno 05
import random
random.seed(2753)
total_numeros = 30000

#req 1
cont_negativos = 0
suma_mayor0 = 0
cont_mayor5000 = 0

# req 2
total_num_divisible3y5 = 0
cont_num_divisible3y5 = 0

# req 3
menor = None

# req 4
cont_negativos_impares = 0

for i in range(total_numeros):
    numeros = random.randint(-15000,15000)
    #req 1
    if numeros < 0:
        cont_negativos += 1
    if numeros >= 0 and numeros < 5000:
        suma_mayor0 += numeros
    if numeros >= 5000 and numeros % 2 != 0:
        cont_mayor5000 += 1

    # req 2
    if numeros < 0:
        if numeros % 3 == 0 and numeros % 5 == 0:
            total_num_divisible3y5 += numeros
            cont_num_divisible3y5 += 1
    # req 3
    if numeros > 0:
        if numeros % 3 == 0 and numeros % 4 != 0:
            if menor is None or numeros < menor:
                menor = numeros
    # req 4
    if numeros < 0 and numeros % 2 != 0:
        cont_negativos_impares += 1

# req 1
print(cont_negativos)
print(suma_mayor0)
print(cont_mayor5000)

# req 2
if cont_num_divisible3y5 != 0:
    promedio_2 = total_num_divisible3y5 // cont_num_divisible3y5
else:
    promedio_2 = 0
print(promedio_2)
# req 3
print(menor)
# req 4
porcentaje_4 = (cont_negativos_impares * 100) // total_numeros
print(f"{porcentaje_4}%")
