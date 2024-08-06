
def opc_a():
    while True:
        valor = int(input("Ingrese un valor positivo entre 1 y 10, con (-1) cierra\Ingrese número: "))
        if valor != -1:
            if 1 <= valor <= 10:
                for n in range(10):
                    multiplicacion = valor * (n+1)
                    print(f"{valor}x{n+1} = {multiplicacion}")
            else:
                print("Ingrese un valor que este en el intervalo de [1, 10]")
        else:
            break

def opc_b():
    mayor = None
    menor = None
    while True:
        numero = int(input("Ingresar un número: "))
        if numero > 0:
            if mayor is None or numero > mayor:
                mayor = numero
            if menor is None or numero < menor:
                menor = numero
        elif numero == 0:
            break
        else:
            print("Ingrese un número valido, solo se permite números positivos.")
    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}")

def opc_c():
    valor_a = int(input("Ingrese el valor a: "))
    valor_b = int(input("Ingrese valor b, este debe ser mayor que a: "))
    suma = 0
    if valor_a > 0 and valor_b > valor_a:
        for i in range(valor_a, valor_b, valor_a):
            suma += i
        print(f"Resultado de suma: {suma}")
    else:
        print("valor a debe ser positivo y valor b debe ser mayor que a")


def opc_d():
    texto = input("Ingresar texto, este debe terminar con punto: ")
    cont_vocal = 0
    cont_palabras = 0
    if texto[-1] == ".":
        anterior = ""
        for caracter in texto:
            if caracter != " " and caracter != ".":
                anterior = caracter
            else:
                if anterior.lower() in 'aeiouáéíóú':
                    cont_vocal += 1
                cont_palabras += 1
        porcentaje = 0
        if cont_palabras != 0:
            porcentaje = (cont_vocal/cont_palabras)*100
        print(f"Palabras que terminan en vocal: {cont_vocal}")
        print(f"Porcentaje {round(porcentaje, 2)}%")

    else:
        print("El texto debe terminar con un punto.")


def main():
    while True:
        print("Menu\na) Tablas\nb) Mayor y menor\nc) Múltiplos\nd) Texto\ne) Salir.")
        opcion = input("Seleccione una opción: ")
        if opcion.lower() == "a":
            opc_a()
        elif opcion.lower() == "b":
            opc_b()
        elif opcion.lower() == "c":
            opc_c()
        elif opcion.lower() == "d":
            opc_d()
        elif opcion.lower() == "e":
            break
        else:
            print("Opción invalida")

if __name__ == "__main__":
    main()

