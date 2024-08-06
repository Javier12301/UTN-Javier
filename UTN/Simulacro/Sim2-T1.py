def lectura_archivo():
    archivo = open("entrada2.txt", "r",encoding="utf-8")
    leer_linea = archivo.read()
    archivo.close()
    return leer_linea

def detectar_tipo_char(caracter):
    if caracter.lower() in "aeiouáéíóú":
        return 'vocal'
    elif caracter.lower() in 'bcdfghjklmnñpqrstvwxyz':
        return 'consonante'
    elif caracter.isdigit():
        return 'digito'
    else:
        return None

def main():
    linea = lectura_archivo()
    # Contadores
    cont_r1 = cont_palabra_r2 = cont_letras_r2 = cont_r3 = cont_r4 = 0

    # Ayudas
    cont_letras = cont_palabras = cont_vocal = cont_consonante = cont_digitos = 0
    anterior = None
    # R2
    cont_r = cont_e = 0
    # R3
    flag_inicio_con_vocal_r3 = False
    caracter_vocal_inicial_r3 = None
    # R4
    flag_tiene_expresion_fi = flag_tiene_n_o_t = False

    for caracter in linea:
        if caracter != " " and caracter != ".":
            cont_letras += 1
            # ayuda -> contador consonante, vocal o digito
            tipo_caracter = detectar_tipo_char(caracter)
            if tipo_caracter == 'consonante':
                cont_consonante += 1
            elif tipo_caracter == 'vocal':
                cont_vocal += 1
            elif tipo_caracter == 'digito':
                cont_digitos += 1

            #r2
            if caracter.lower() == 'r':
                cont_r += 1
            elif caracter.lower() == 'e':
                cont_e += 1

            #r3
            if anterior is None and tipo_caracter == 'vocal':
                # Se crea el flag para avisar que comienza con vocal
                # En palabras se deberá verificar si termina con vocal
                # USANDO EL ANTERIOR, también verificar que no sean iguales
                flag_inicio_con_vocal_r3 = True
                caracter_vocal_inicial_r3 = caracter.lower()
            #r4
            if anterior is not None:
                if anterior.lower() == "f" and caracter.lower() == "i":
                    flag_tiene_expresion_fi = True
                if caracter.lower() == "n" or caracter.lower() == "t":
                    flag_tiene_n_o_t = True
            anterior = caracter
        else:
            cont_palabras += 1
            #r1
            if cont_letras == 6 and 1 <= cont_vocal <= 2 and cont_digitos >= 1:
                cont_r1 += 1
            #r2
            if cont_r == 1 and cont_e >= 2:
                cont_palabra_r2 += 1
                cont_letras_r2 += cont_letras
            #r3
            if flag_inicio_con_vocal_r3 and caracter_vocal_inicial_r3 != anterior.lower():
                if detectar_tipo_char(anterior) == 'vocal':
                    cont_r3 += 1
            #r4
            if flag_tiene_expresion_fi and flag_tiene_n_o_t:
                cont_r4 += 1

            flag_inicio_con_vocal_r3 = False
            flag_tiene_expresion_fi = False
            flag_tiene_n_o_t = False
            anterior = None
            caracter_vocal_inicial_r3 = None
            cont_vocal = 0
            cont_consonante = 0
            cont_digitos = 0
            cont_letras = 0
    # Determinar resultados
    # promedio r2
    promedio_r2 = 0
    if cont_palabra_r2 != 0:
        promedio_r2 = calcular_promedio(cont_letras_r2, cont_palabra_r2)
    resultados(cont_r1, promedio_r2, cont_r3, cont_r4)

def calcular_promedio(cantidad,total):
    promedio = 0
    if total != 0:
        promedio = int(cantidad / total)
    return promedio
def resultados(r1,r2,r3,r4):
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)






if __name__ == "__main__":
    main()