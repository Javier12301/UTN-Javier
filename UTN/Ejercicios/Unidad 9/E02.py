# Secuencia de números aleatorios
import random
random.seed(10)

cont_termina_5 = 0
# porc
cont_numpar = 0
# menor
menor = None
# d
flag_primera_recorrido = True
primer_num = None
cont_primernumero = 0
n = int(input("Ingrese la cantidad de números en la sucesión: "))
if n > 0:
    for i in range(n):
        num = random.randint(1,500)
        if num % 10 == 5:
            cont_termina_5 += 1
        if num % 2 == 0:
            cont_numpar += 1
        if menor is None or (num < menor and num % 3 == 0):
            menor = num
        if flag_primera_recorrido:
            primer_num = num
            flag_primera_recorrido = False
        if num == primer_num:
            cont_primernumero += 1
    # resultado
    print(f"Número terminan en 5: {cont_termina_5}")
    porc = (cont_numpar / n) * 100
    print(f"Porcentaje númerosp ares: {porc}")
    print(f"Número menor multiplo de 3: {menor}")
    print(f"El primer valor el cual es: {primer_num} apareció en total: {cont_primernumero}")
else:
    print("Debe ingersar un número mayor a 0")
