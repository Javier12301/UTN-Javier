i = 1

cont_div4 = 0
mayor_impar = None
primer_numero = None
cont_primer_numero = 0
cont_1_2_3 = 0

sucesion_1 = False
sucesion_2 = False


while True:
    numero = int(input(f"{i}. Ingrese número (0 termina carga): "))
    i += 1
    if numero != 0:
        if numero % 4 == 0:
            cont_div4 += 1
        if numero % 2 != 0:
            if mayor_impar is None or numero > mayor_impar:
                mayor_impar = numero
        if primer_numero is None:
            primer_numero = numero
        if numero == primer_numero:
            cont_primer_numero += 1
        if numero == 1:
            sucesion_1 = True
        elif numero == 2 and sucesion_1:
            sucesion_2 = True
        elif numero == 3 and sucesion_1 and sucesion_2:
            cont_1_2_3 += 1
        else:
            sucesion_1 = False
            sucesion_2 = False
    else:
        break

# Resultado
print(f"a. {cont_div4}")
print(f"b. {mayor_impar}")
print(f"c. {cont_primer_numero}")
print(f"d. {cont_1_2_3}")
