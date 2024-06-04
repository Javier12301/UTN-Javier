import random
random.seed(1157)

cont_1000 = 0
suma_15000 = 0
cont_30000 = 0

# req 2
total_divisible7 = 0
cont_divisible7 = 0

# req 3
menor = None

# req 4
total_pares = 0
cont_pares = 0



for i in range(17000):
    numeros = random.randint(1000,37000)
    # requerimiento 1
    if numeros >= 1000 and numeros < 15000:
        cont_1000 += 1
    if numeros >= 15000 and numeros < 30000:
        suma_15000 += numeros
    if numeros >= 30000:
        cont_30000 += 1

    # requerimiento 2
    if numeros % 7 == 0 and numeros % 3 != 0:
        total_divisible7 += numeros
        cont_divisible7 += 1

    # requerimiento 3
    if numeros % 2 != 0:
        if menor is None or numeros < menor:
            menor = numeros

    # requerimiento 4
    if numeros % 2 == 0:
        total_pares += numeros
        cont_pares += 1

# Salidas
# req 1
print("Requerimiento 1")
print(cont_1000)
print(suma_15000)
print(cont_30000)
print("\n")

print("Requerimiento 2")
# promedio entero
promedio_req2 = total_divisible7 / cont_divisible7
print(f"Promedio entero: {int(promedio_req2)}")
print("\n")

print("Requerimiento 3")
print(f"{menor}")
print("\n")


print("Requerimiento 4")
porcentaje_req4 = (cont_pares * 100) // 17000
print(f"Porcentaje req4: {porcentaje_req4}")



