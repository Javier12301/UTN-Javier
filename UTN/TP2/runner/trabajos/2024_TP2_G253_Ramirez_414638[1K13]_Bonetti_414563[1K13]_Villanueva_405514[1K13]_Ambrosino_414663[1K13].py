# Acumuladores de tipo de envio
ccs = 0
ccc = 0
cce = 0
# Funciones
def identificar_control(linea):
    if "hc" in linea.lower():
        return "Hard Control"
    else:
        return "Soft Control"

def obtener_cp(linea):
    cp = linea[0:9].strip()
    return cp
def obtener_provincia(cp):
    if len(cp) == 8 and cp[0].isalpha() and cp[0] != "O" and cp[0] != "I" and cp[1:4].isdigit() and [cp[5:].isalpha()]:
        # Detección provincias
        destino = "Argentina"
        if (cp[0] == "B"):
            provincia = "Buenos Aires"
        else:
            provincia = "No aplica"
        return provincia
def identificar_destino(cp):
    if len(cp) == 8 and cp[0].isalpha() and cp[0] != "O" and cp[0] != "I" and cp[1:4].isdigit() and cp[5:].isalpha():
        destino = "Argentina"
    elif len(cp) == 4 and cp.isdigit():
        destino = "Bolivia"
    elif len(cp) == 9 and cp[:5].isdigit() and cp[5] == "-" and cp[6:8].isdigit() and cp[8:].isdigit():
        destino = "Brasil"
    elif len(cp) == 7 and cp.isdigit():
        destino = "Chile"
    elif len(cp) == 6 and cp.isdigit():
        destino = "Paraguay"
    elif len(cp) == 5 and cp.isdigit():
        destino = "Uruguay"
    else:
        destino = "Otro"
    return destino

def identificar_direccion(linea):
    direccion = linea[9:29].strip().replace(".","")
    return direccion

def identificar_tipo_envio(linea):
    tipo_envio = linea[29]
    return int(tipo_envio)

def identificar_tipo_pago(linea):
    tipo_pago = linea[30]
    return int(tipo_pago)

def extraer_palabras(direccion):
    palabras = ()
    palabra_actual = ""

    for char in direccion:
        # Detectar espacio, una palabras siempre termina despues del espacio
        if char == ' ':
            if palabra_actual:
                palabras += (palabra_actual,)
                palabra_actual = ""
        else:
            palabra_actual += char

    if palabra_actual:
        palabras += (palabra_actual,)

    return palabras

# Hipolito Yrigoyen 312
def validar_direccion(direccion):
    # Almacenar palabras en tuplas, con el fin de poder recorrer y verificar si existen mayusculas
    palabras_tupla = extraer_palabras(direccion)
    hay_palabra_digitos = False

    for i in range(len(direccion) - 1):
        if direccion[i].isupper() and direccion[i + 1].isupper():
            return False
    # Recorrer la tupla de palabras y verificar si la palabra está compuesta de letras o digitos.
    # O sea: Hertz 4236
    for palabra in palabras_tupla:
        if not (palabra.isalpha() or palabra.isdigit()):
            return False
        if palabra.isdigit():
            hay_palabra_digitos = True

    return hay_palabra_digitos

def configurar_tipo_envio(tipo):
    inicial = 0
    if 0 <= tipo <= 6:
        if tipo == 0:
            inicial = 1100
        elif tipo == 1:
            inicial = 1800
        elif tipo == 2:
            inicial = 2450
        elif tipo == 3:
            inicial = 8300
        elif tipo == 4:
            inicial = 10900
        elif tipo == 5:
            inicial = 14300
        else:
            inicial = 17900
    return int(inicial)

def configurar_envios_internacionales(destino, cp , inicial):
    if destino == "Bolivia" or destino == "Paraguay":
        inicial *= 1.20
    elif destino == "Uruguay":
        if cp[0] == "1":
            inicial *= 1.20
        else:
            inicial *= 1.25
    elif destino == "Chile":
        inicial *= 1.25
    elif destino == "Brasil":
        if cp[0] in ["0", "1", "2", "3"]:
            inicial *= 1.25
        elif cp[0] in ["4", "5", "6", "7"]:
            inicial *= 1.30
        elif cp[0] in ["8", "9"]:
            inicial *= 1.20
    elif destino == "Otro":
        inicial *= 1.50
    return int(inicial)
def configurar_forma_pago(pago, inicial):
    # Proceso de forma de pago
    # Aplicar descuento
    if pago == 1:
        final = inicial * 0.90
    else:
        final = inicial
    return int(final)

def acumuladores_tipo_envio(tipo_envio):
    global ccs, ccc, cce
    if 0 <= tipo_envio <= 2:
        ccs += 1
    elif 3 <= tipo_envio <= 4:
        ccc += 1
    else:
        cce += 1

# Mayor carta
def obtener_tipo_carta_mayor_envios():
    global ccs, cce, ccc
    if (ccs >= cce and ccs >= ccc):
        mayor = "Carta Simple"
    elif cce >= ccs and cce >= ccc:
        mayor = "Carta Expresa"
    else:
        mayor = "Carta Certificada"
    return mayor

def calcular_porcentaje(cont_total_envios_ext, cont_total_envios):
    return int((cont_total_envios_ext * 100) / cont_total_envios)

def calcular_promedio(final_buenos_aires, cont_buenos_aires):
    if cont_buenos_aires != 0:
        prom = int(final_buenos_aires / cont_buenos_aires)
    else:
        prom = 0
    return prom

def leer_txt(archivo_txt):
    archivo = open(archivo_txt, "r", encoding="utf-8")
    return archivo

def init():
    archivo = leer_txt("envios.txt")
    # Variables locales para manejo de funcionalidades
    cedvalid = 0
    cedinvalid = 0
    imp_acu_total = 0
    cant_primer_cp = 0
    # Variable menor, se declara None para decir que no existe un menor todavía.
    menimp = None
    porc = 0
    prom = 0
    final_buenos_aires = 0
    cont_buenos_aires = 0
    cont_total_envios_ext = 0
    cont_total_envios = 0
    # Banderas
    flag_control = False
    flag_primer_cp = False
    # Obtener arhivo txt, y leer linea por linea
    for linea in archivo:
        # Iniciar variables para indicar precio inicial y final del envio.
        inicial = 0
        final = 0
        # Limpiar el "enter" que genera la linea para la siguiente fila.
        linea = linea.replace("\n", "")
        # R1 identificar el Control del txt.
        if not flag_control:
            control = identificar_control(linea)
            flag_control = True
            flag_primer_cp = True
            continue
        # Obtener datos de linea
        cp = obtener_cp(linea)
        provincia = obtener_provincia(cp)
        destino = identificar_destino(cp)
        direccion = identificar_direccion(linea)
        tipo_envio = identificar_tipo_envio(linea)
        tipo_pago = identificar_tipo_pago(linea)
        #R9 Y R10
        if flag_primer_cp:
            primer_cp = cp
            flag_primer_cp = False
        if cp == primer_cp:
            cant_primer_cp += 1
        # Según tipo de control, verificar o no dirección
        inicial = configurar_tipo_envio(tipo_envio)
        if destino != "Argentina":
            inicial = configurar_envios_internacionales(destino, cp, inicial)
        final = configurar_forma_pago(tipo_pago, inicial)
        if control.lower() == "hard control":
            direccion_valida = validar_direccion(direccion)
            cont_total_envios += 1
            if direccion_valida:
                if destino != "Argentina":
                    cont_total_envios_ext += 1
                cedvalid += 1
                imp_acu_total += final
                acumuladores_tipo_envio(tipo_envio)
                # R14
                if provincia == "Buenos Aires":
                    final_buenos_aires += final
                    cont_buenos_aires += 1
            else:
                cedinvalid += 1
        else:
            cont_total_envios += 1
            if destino != "Argentina":
                cont_total_envios_ext += 1
            cedvalid += 1
            # Configuraciones de tipo de envio, internacional y pago
            imp_acu_total += final
            acumuladores_tipo_envio(tipo_envio)
            # R14
            if provincia == "Buenos Aires":
                final_buenos_aires += final
                cont_buenos_aires += 1
        tipo_mayor = obtener_tipo_carta_mayor_envios()
        # R11 Y R12
        if destino == "Brasil":
            if menimp is None or final < menimp:
                menimp = final
                mencp = cp
        # R13 Y 14
        porc = calcular_porcentaje(cont_total_envios_ext, cont_total_envios)
        prom = calcular_promedio(final_buenos_aires, cont_buenos_aires)
    resultado(control, cedvalid, cedinvalid, imp_acu_total, ccs, ccc, cce, tipo_mayor, primer_cp, cant_primer_cp, menimp, mencp, porc, prom)

# Salida
def resultado(control, cedvalid, cedinvalid, imp_acu_total, ccs, ccc, cce, tipo_mayor, primer_cp, cant_primer_cp, menimp, mencp, porc, prom):
    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
    print(' (r5) - Cantidad de cartas simples:', ccs)
    print(' (r6) - Cantidad de cartas certificadas:', ccc)
    print(' (r7) - Cantidad de cartas expresas:', cce)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
    print('(r14) - Importe final promedio de los envios Buenos Aires:', prom)

if __name__ == '__main__':
    init()

