
texto = input("Ingrese un texto: ")
if texto[-1] != '.':
    texto += '.'
cont_letras = 0
anterior = ''
cont_palabras = 0
cont_letras_palabra = 0
cont_palabras_mas_4_letras = 0
cont_letraXoY = 0
cont_expresion_mo = 0
cont_palabras_mo = 0
flag_XoY_una_vez = False
for caracter in texto:
    if caracter != ' ' and caracter != '.':
        cont_letras += 1
        cont_letras_palabra += 1
        if (caracter == "x" or caracter == "y") and not flag_XoY_una_vez:
            cont_letraXoY += 1
            flag_XoY_una_vez = True
        if anterior.lower() == "m" and caracter.lower() == "o":
            cont_expresion_mo += 1
        anterior = caracter
    else:
        flag_XoY_una_vez = False
        cont_palabras += 1
        if cont_letras_palabra > 4:
            cont_palabras_mas_4_letras += 1
        if cont_expresion_mo == 1:
            cont_palabras_mo += 1
        cont_expresion_mo = 0
        cont_letras_palabra = 0

print(f"Palabras con más de 4 letras: {cont_palabras_mas_4_letras}")
print(f"Palabras que tenian al menos una vez letra x o y: {cont_letraXoY}")
promedio = 0
if cont_palabras != 0:
    promedio = round(cont_letras / cont_palabras, 2)
print(f"El promedio de letras por palabras es: {promedio}%")
print(f"Cuantas palabras tenian una sola vez \"mo\": {cont_palabras_mo}")
