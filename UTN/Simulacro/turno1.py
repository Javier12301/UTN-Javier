# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para cacular el promedio entero entre sus parámetros.
def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r2 = r3 = r4 = 0

    # contador de letras en una palabra...
    cl = 0

    # item 1: contador de vocales y contador de dígitos en una palabra...
    cv = cd = 0

    # item 2: contador de letras "r" y contador de letras "e"...
    cr = ce = 0

    # item 2: acumulador de letras y contador de palabras...
    clre = cpre = 0

    # item 4: flags para f, fi, y (n - t)...
    sf = sfi = snt = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada2.txt")
    texto = m.read()
    m.close()

    # texto = "."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if cl == 6 and cv != 0 and cv <= 2 and cd >= 1:
                    r1 += 1

                # item 2...
                if cr == 1 and ce >= 2:
                    clre += cl
                    cpre += 1

                # item 3...
                if pl.lower() != ul.lower() and es_vocal(pl) and es_vocal(ul):
                    r3 += 1

                # item 4...
                if sfi and snt:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            cv = cd = 0

            # item 2...
            cr = ce = 0

            # item 4...
            sf = sfi = snt = False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if es_vocal(car):
                cv += 1
            elif es_digito(car):
                cd += 1

            # item 2...
            if car in "rR":
                cr += 1
            elif car in "eEéÉ":
                ce += 1

            # item 3...
            if cl == 1:
                # guardar la primera letra...
                pl = car

            # item 4...
            if car in "fF":
                sf = True
            else:
                if sf and car in "iíIÍ":
                    sfi = True
                sf = False

            if car in "nNtT":
                snt = True

            # item 3...
            # guardar la última letra...
            ul = car

    # cálculo del promedio para r2...
    r2 = calcular_promedio(clre, cpre)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
