# bcdfghijklmnñpqrstvwxyz
# DEF CON RETORNOS
def detectar_consonante_o_vocal(caracter):
    if caracter.lower() in "bcdfghijklmnñpqrstvwxyz":
        return "consonante"
    elif caracter.lower() in "aeiou":
        return "vocal"

# DEF VOID -> NO RETORNA NADA
def suma(a,b):
    resultado = a + b
    print(resultado)

def main():
    # r -> solo lectura
    # w -> escritura
    archivo = open("prueba.txt", "r", encoding="utf-8")
    fila = archivo.read()
    for caracter in fila:
        # aqui es una letra
        if caracter != " " and caracter != ".":
           tipo_caracter = detectar_consonante_o_vocal(caracter)
        # Cuando salta else siempre es una palabra
        else:
            print("siguiente palabra\n")

if __name__ == "__main__":
    main()
