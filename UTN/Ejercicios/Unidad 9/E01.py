# Generar sucesión mil números enteros
import random
random.seed(11)
# Establecer números
n = 1000
# Contadores
cont_num_div4 = 0
cont_num_div4y8 = 0
# Prom
sum_num_may2000 = 0
cont_num_may2000 = 0
# Menores
primer_valor = None
cont_menores = 0
# ¿Aparecen valores extremos del intervalo (1,2500)?
valores_extremos = False

# arranque
for i in range(n):
    num = random.randint(1, 2500)
    if num % 4 == 0:
        if num % 8 == 0:
            cont_num_div4y8 += 1
        else:
            cont_num_div4 += 1
    if num > 2000:
        sum_num_may2000 += num
        cont_num_may2000 += 1
    if primer_valor is None:
        primer_valor = num
    else:
        if num < primer_valor:
            cont_menores += 1
    if num == 1 or num == 2500:
        valores_extremos = True

# Resultados
print(cont_num_div4)
print(cont_num_div4y8)
# promedio
if cont_num_may2000 != 0:
    promedio_may2000 = int(sum_num_may2000 / cont_num_may2000)
else:
    promedio_may2000 = 0
print(promedio_may2000)

# numeros menores al primer valor
print(primer_valor)
porc_menores = (cont_menores / n) * 100
print(fr"Números menores al primer valor: {cont_menores} y represental el {porc_menores}%")
if valores_extremos:
    print("Si aparecieron")
else:
    print("No aparecieron")
