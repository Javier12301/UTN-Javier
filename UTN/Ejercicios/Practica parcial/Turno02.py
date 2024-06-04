import random
random.seed(973)

total_numeros = 14000

#Req 1
cont_num_menores11000 = 0
cont_num_mayores11000 = 0
cont_num_mayores17000 = 0

# req 2
total_divisible9 = 0
cont_divisible9 = 0

# req 3
mayor_1000y14000 = None

# Req 4
cont_divsible6 = 0

for i in range(total_numeros):
    numeros = random.randint(100,21100)

    #Req 1
    if numeros <= 11000:
        cont_num_menores11000 += 1
    if numeros > 11000 and numeros < 17000 and (numeros % 3 == 0 and numeros % 8 == 0):
        cont_num_mayores11000 += 1
    if numeros >= 17000:
        cont_num_mayores17000 += 1

    #Req 2
    if numeros % 9 == 0 and numeros <= 15000:
        cont_divisible9 += 1
        total_divisible9 += numeros

    # Req 3
    # 1000 <= numeros <= 14000
    if numeros >= 1000 and numeros <= 14000:
        if mayor_1000y14000 is None or numeros > mayor_1000y14000:
            mayor_1000y14000 = numeros

    # Req 4
    if numeros % 6 == 0:
        cont_divsible6 += 1


# Salidas
# 1
print(cont_num_menores11000)
print(cont_num_mayores11000)
print(cont_num_mayores17000)

# 2
# calculo promedio
if cont_divisible9 != 0:
    promedio_2 = total_divisible9 // cont_divisible9
print(promedio_2)
# 3
print(mayor_1000y14000)

#4
porcentaje_4 = (cont_divsible6 * 100) // total_numeros
print(porcentaje_4)