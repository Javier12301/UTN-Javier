


def main():
    texto = input("Ingresar texto: ")
    if texto[-1] != ".":
        texto += "."
    cont_palabras_iniCons_finVocal = 0
    cont_palabras_poseen_li = 0
    flag_tiene_li = False
    cont_letras = 0
    cont_palabras = 0
    cont_palabras_con_menos_letras = 0
    flag_inicio_consonante = False
    flag_inicio_palabra = True
    flag_fin_vocal = False
    anterior = ""
    for caracter in texto:
        if caracter != " " and caracter != ".":
            cont_letras += 1
            if flag_inicio_palabra:
                if caracter.lower() in "bcdfghjklmnñpqrstvwxyz":
                    flag_inicio_consonante = True
            if cont_letras > 3:
                if anterior.lower() == "l" and caracter.lower() == "i":
                    flag_tiene_li = True
            anterior = caracter
        else:
            if flag_inicio_consonante and anterior.lower() in "aeiou":
                cont_palabras_iniCons_finVocal += 1
            if flag_tiene_li:
                cont_palabras_poseen_li += 1
                flag_tiene_li = False
            if cont_letras < 4:
                cont_palabras_con_menos_letras += 1
            cont_palabras += 1
            cont_letras = 0
            anterior = ""
    print(f"a: {cont_palabras_iniCons_finVocal}")
    print(f"b: {cont_palabras_poseen_li}")
    porcentaje = 0
    if cont_palabras != 0:
        porcentaje = round((cont_palabras_con_menos_letras/cont_palabras)*100)
    print(f"c: {porcentaje}%")



if __name__ == "__main__":
    main()