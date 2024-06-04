import random

random.seed(49)

total_numeros = 20000

# req 1
cont_multiplo5 = 0
cont_multiplo7 = 0
cont_multiplo9 = 0

#req 2
mayor = None

#req 3
cont_numpares_menor15000 = 0



for i in range(total_numeros):
    numeros = random.randint(1,45000)
    # req 1
    if numeros % 5 == 0:
        cont_multiplo5 += 1
    if numeros % 7 == 0:
        cont_multiplo7 += 1
    if numeros % 9 == 0:
        cont_multiplo9 += 1

    # req 2
    if 5 <= numeros % 10 <= 8:
        if mayor is None or numeros > mayor:
            mayor = numeros
    # req 3
    if numeros % 2 == 0:
        if numeros < 15000:
            # req 3 y 4
            cont_numpares_menor15000 += 1

# req 1
print(cont_multiplo5)
print(cont_multiplo7)
print(cont_multiplo9)

# req 2
print(mayor)

# req 3
print(cont_numpares_menor15000)

# req 4
porcentaje_4 = (cont_numpares_menor15000 * 100) // total_numeros
print(porcentaje_4)
