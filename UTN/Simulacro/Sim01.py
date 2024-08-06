def cargar_archivo():
    # r = Modo lectura
    # LEER ARCHIVO
    archivo = open("entrada.txt", "r", encoding="utf-8")
    return archivo


def detectar_tipo_caracter(caracter):
    if caracter.lower() in "bcdfghjklmnñpqrstvwxyz":
        return "consonante"
    elif caracter.lower() in "aeiouáéíóú":
        return "vocal"
    return None

def resultado(r1, r2, r3, r4):
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


def main():
    # contadores
    cont_letras = cont_palabras = cont_consonante = cont_vocal = 0
    cont_1 = cont_2 = cont_letras_3 = cont_palabras_3 = sum_3_char = cont_4 = 0
    cont_veces_repetidas_d_y_vocal_4 = 0
    # flags
    flag_inicio_impar_1 = flag_inicio_vocal_2 = flag_tiene_b_2 = flag_tiene_m = flag_tiene_a = False
    flag_dos_veces_d_y_vocal_4 = False
    # ayudas
    anterior = mayor_2 = None
    archivo = cargar_archivo()
    linea = archivo.read()
    archivo.close()

    for caracter in linea:
        if caracter != " " and caracter != ".":
            cont_letras += 1
            # tipo char
            tipo_caracter = detectar_tipo_caracter(caracter)
            if tipo_caracter == "consonante":
                cont_consonante += 1
            elif tipo_caracter == "vocal":
                cont_vocal += 1
            # R1
            if anterior is None and caracter.isdigit():
                if int(caracter) % 2 != 0:
                    flag_inicio_impar_1 = True
            else:
                if flag_inicio_impar_1 and (not caracter.isalpha() or not caracter.islower()):
                    flag_inicio_impar_1 = False
            # R2
            if anterior is None and caracter.isalpha() and detectar_tipo_caracter(caracter) == 'vocal':
                flag_inicio_vocal_2 = True
            if flag_inicio_vocal_2 and caracter.lower() == "b":
                flag_tiene_b_2 = True
            # R3
            if caracter.lower() == "m":
                flag_tiene_m = True
            elif caracter.lower() == "a":
                flag_tiene_a = True
            # R4
            if anterior is not None:
                if anterior.lower() == "d" and detectar_tipo_caracter(caracter) == 'vocal':
                    cont_veces_repetidas_d_y_vocal_4 += 1
                    if cont_veces_repetidas_d_y_vocal_4 >= 2:
                        flag_dos_veces_d_y_vocal_4 = True
            anterior = caracter
        else:
            anterior = None
            cont_palabras += 1
            # R1
            if flag_inicio_impar_1:
                cont_1 += 1
                flag_inicio_impar_1 = False
            # R2
            if flag_inicio_vocal_2 and flag_tiene_b_2:
                if mayor_2 is None or cont_letras > mayor_2:
                    mayor_2 = cont_letras
            flag_inicio_vocal_2 = False
            flag_tiene_b_2 = False
            # R3
            if not flag_tiene_a and not flag_tiene_m:
                if cont_consonante > cont_vocal:
                    cont_letras_3 += cont_letras
                    cont_palabras_3 += 1
            flag_tiene_a = False
            flag_tiene_m = False
            # R4
            if flag_dos_veces_d_y_vocal_4:
                cont_4 += 1
            flag_dos_veces_d_y_vocal_4 = False
            cont_letras = cont_consonante = cont_vocal = 0

    # calcular promedio r3
    promedio = 0
    if cont_palabras_3 != 0:
        promedio = int(cont_letras_3 / cont_palabras_3)

    resultado(cont_1, mayor_2, promedio, cont_4)


if __name__ == "__main__":
    main()
