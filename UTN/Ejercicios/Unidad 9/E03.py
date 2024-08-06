# Secuencia, menu y texto

def secuencia_num():
    cont_multiplo3y5 = 0
    while True:
        n = int(input("Ingresar números a procesar: "))
        if n > 0:
            break
        else:
            print("Ingrese un número mayor a 0 para continuar")
    for i in range(n):
        numero = int(input(f"{i + 1}. Ingresar número: "))
        if numero % 3 == 0 or numero % 5 == 0:
            cont_multiplo3y5 += 1
    # Resultados
    print(f"Cantidad números múltiplo de 3: {cont_multiplo3y5}")
    porcentaje_mul3y5 = round((cont_multiplo3y5 / n) * 100, 2)
    print(f"Porcentaje números multiplo 3: {porcentaje_mul3y5}%")


def ingresar_texto():
    cont_palabras_de_mas4_letras = 0
    cont_letras = 0
    texto = input("Ingresar un texto: ")
    if texto[-1] != ".":
        texto += '.'

    for caracter in texto:
        if caracter != " " and caracter != '.':
            cont_letras += 1
        else:
            if cont_letras > 4:
                cont_palabras_de_mas4_letras += 1
            cont_letras = 0
    print(f"Hay {cont_palabras_de_mas4_letras} palabras que terminan con más de 4 letras.")


def ingresar_nombre_notas():
    alumno1 = input("Ingrese nombre alumno: ")
    nota1 = int(input("Ingrese nota: "))
    alumno2 = input("Ingrese nombre alumno: ")
    nota2 = int(input("Ingrese nota: "))
    alumno3 = input("Ingrese nombre alumno: ")
    nota3 = int(input("Ingrese nota: "))

    if nota1 < nota2 and nota1 < nota3:
        peor_nota = alumno1
    elif nota2 < nota1 and nota2 < nota3:
        peor_nota = alumno2
    else:
        peor_nota = alumno3
    print(f"La peor nota es del alumno: {peor_nota}")
def main():
    # Arranque de menu
    while True:
        print("/"*8 ,"Menu de Opciones","/"*8)
        print("Opciones:\na) Ingresar secuencia de n números\nb) Ingresar un texto\nc) Ingresar nombre y notas finales\nd)Salir.")
        opcion = input("Seleccione una opción: ")
        if opcion.lower() == "a":
            secuencia_num()
        elif opcion.lower() == "b":
            ingresar_texto()
        elif opcion.lower() == "c":
            ingresar_nombre_notas()
        elif opcion.lower() == "d":
            print("¡Gracias por usar el menu!.")
            break
        else:
            print("Seleccione una opción valida.")
            input("Presione cualquier tecla para continuar...")


if __name__ == "__main__":
    main()