# Variables por ahora
control = ""
cedvalid = 0
cedinvalid = 0
imp_acu_total = 0
ccs = 0
ccc = 0
cce = 0
tipo_mayor = ""
primer_cp = ""
cant_primer_cp = 0
menimp = None
mencp = ""
porc = 0
prom = 0
final_buenos_aires = 0
cont_buenos_aires = 0

# Funciones
def identificar_control(contenido):
    # leer primera linea
    linea_timestamp = contenido.split("\n")[0]
    if "hc" in linea_timestamp.lower():
        return "Hard Control"
    else:
        return "Soft Control"

def obtener_cp(linea):
    cp = linea[0:9].strip()
    return cp
def obtener_provincia(cp):
    if len(cp) == 8 and cp[0].isalpha and cp[0] != "O" and cp[0] != "I" and cp[1:4].isdigit() and [cp[5:].isalpha]:
        # Detección provincias
        destino = "Argentina"
        if (cp[0] == "C"):
            provincia = "Ciudad Autónoma de Buenos Aires"
        elif (cp[0] == "B"):
            provincia = "Buenos Aires"
        elif (cp[0] == "K"):
            provincia = "Catamarca"
        elif (cp[0] == "H"):
            provincia = "Chaco"
        elif (cp[0] == "U"):
            provincia = "Chubut"
        elif (cp[0] == "X"):
            provincia = "Córdoba"
        elif (cp[0] == "W"):
            provincia = "Corrientes"
        elif (cp[0] == "E"):
            provincia = "Entre Ríos"
        elif (cp[0] == "P"):
            provincia = "Formosa"
        elif (cp[0] == "Y"):
            provincia = "Jujuy"
        elif (cp[0] == "L"):
            provincia = "La Pampa"
        elif (cp[0] == "F"):
            provincia = "La Rioja"
        elif (cp[0] == "M"):
            provincia = "Mendoza"
        elif (cp[0] == "N"):
            provincia = "Misiones"
        elif (cp[0] == "Q"):
            provincia = "Neuquén"
        elif (cp[0] == "R"):
            provincia = "Rio Negro"
        elif (cp[0] == "A"):
            provincia = "Salta"
        elif (cp[0] == "J"):
            provincia = "San Juan"
        elif (cp[0] == "D"):
            provincia = "San Luis"
        elif (cp[0] == "Z"):
            provincia = "Santa Cruz"
        elif (cp[0] == "S"):
            provincia = "Santa Fe"
        elif (cp[0] == "G"):
            provincia = "Santiago del Estero"
        elif (cp[0] == "V"):
            provincia = "Tierra del Fuego"
        elif (cp[0] == "T"):
            provincia = "Tucumán"
        else:
            provincia = "No aplica"
        return provincia
def identificar_destino(cp):
    if len(cp) == 8 and cp[0].isalpha and cp[0] != "O" and cp[0] != "I" and cp[1:4].isdigit() and [cp[5:].isalpha]:
        destino = "Argentina"
    elif len(cp) == 4 and cp[:3].isdigit():
        destino = "Bolivia"
    elif len(cp) == 9 and cp[:4].isdigit() and cp[5] == "-" and cp[6:8].isdigit():
        destino = "Brasil"
    elif len(cp) == 7 and cp[:6].isdigit():
        destino = "Chile"
    elif len(cp) == 6 and cp[:5].isdigit():
        destino = "Paraguay"
    elif len(cp) == 5 and cp[:4].isdigit():
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

def validar_direccion(direccion):
    # Separar en palabras
    palabras = direccion.split()
    for palabra in palabras:
        if not (palabra.isalpha() or palabra.isdigit()):
            return False

    # Verificar si existe dos mayúsculas seguidas
    for i in range(len(direccion) - 1):
        if direccion[i].isupper() and direccion[i + 1].isupper():
            return False

    # Verificar si hay al menos una palabra compuesta solo por digitos
    for palabra in palabras:
        if palabra.isdigit():
            return True
    return False

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

# Entrada de datos
# archivo = open("envios.txt", "r")
with open("envios.txt", "r", encoding="utf-8") as archivo:
    cont_total_envios_ext = 0
    cont_total_envios = 0
    contenido = archivo.read()
    # Identificar timestamp
    control = identificar_control(contenido)
    # Identificar código postal
    # Separamos primero las filas, no tomamos la primera ni la ultima ya que la primera
    # es el Timestamp y la última un salto de linea que se produce de manera automatica
    lineas = contenido.split("\n")[1:-1]
    for i in range(0, len(lineas)):
        inicial = 0
        final = 0
        cp = obtener_cp(lineas[i])
        provincia = obtener_provincia(cp)
        destino = identificar_destino(cp)
        direccion = identificar_direccion(lineas[i])
        tipo_envio = identificar_tipo_envio(lineas[i])
        tipo_pago = identificar_tipo_pago(lineas[i])

        # R9 Y R10
        if i == 0:
            primer_cp = cp
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
        porc = int((cont_total_envios_ext * 100) / cont_total_envios)
        if cont_buenos_aires != 0:
            prom = int(final_buenos_aires / cont_buenos_aires)
        else:
            prom = 0

# Salida
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
