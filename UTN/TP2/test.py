# Acumuladores de tipo de envio
ccs = 0
ccc = 0
cce = 0

# Funciones para identificar y procesar datos
def identificar_control(linea):
    return "Hard Control" if "hc" in linea.lower() else "Soft Control"

def obtener_cp(linea):
    return linea[0:9].strip()

def obtener_provincia(cp):
    if len(cp) == 8 and cp[0].isalpha() and cp[0] not in "OI" and cp[1:4].isdigit() and cp[5:].isalpha():
        return "Buenos Aires" if cp[0] == "B" else "No aplica"

def identificar_destino(cp):
    if len(cp) == 8 and cp[0].isalpha() and cp[0] not in "OI" and cp[1:4].isdigit() and cp[5:].isalpha():
        return "Argentina"
    elif len(cp) == 4 and cp.isdigit():
        return "Bolivia"
    elif len(cp) == 9 and cp[:5].isdigit() and cp[5] == "-" and cp[6:].isdigit():
        return "Brasil"
    elif len(cp) == 7 and cp.isdigit():
        return "Chile"
    elif len(cp) == 6 and cp.isdigit():
        return "Paraguay"
    elif len(cp) == 5 and cp.isdigit():
        return "Uruguay"
    else:
        return "Otro"

def identificar_direccion(linea):
    return linea[9:29].strip().replace(".", "")

def identificar_tipo_envio(linea):
    return int(linea[29])

def identificar_tipo_pago(linea):
    return int(linea[30])

def extraer_palabras(direccion):
    return tuple(direccion.split())

def validar_direccion(direccion):
    palabras_tupla = extraer_palabras(direccion)
    if any(palabra.isdigit() for palabra in palabras_tupla):
        return all(palabra.isalpha() or palabra.isdigit() for palabra in palabras_tupla) and all(
            not (direccion[i].isupper() and direccion[i + 1].isupper()) for i in range(len(direccion) - 1)
        )
    return False

def configurar_tipo_envio(tipo):
    tarifas = [1100, 1800, 2450, 8300, 10900, 14300, 17900]
    return tarifas[tipo] if 0 <= tipo <= 6 else 0

def configurar_envios_internacionales(destino, cp, inicial):
    if destino in ["Bolivia", "Paraguay"]:
        inicial *= 1.20
    elif destino == "Uruguay":
        inicial *= 1.20 if cp[0] == "1" else 1.25
    elif destino == "Chile":
        inicial *= 1.25
    elif destino == "Brasil":
        if cp[0] in "0123":
            inicial *= 1.25
        elif cp[0] in "4567":
            inicial *= 1.30
        elif cp[0] in "89":
            inicial *= 1.20
    elif destino == "Otro":
        inicial *= 1.50
    return int(inicial)

def configurar_forma_pago(pago, inicial):
    return int(inicial * 0.90) if pago == 1 else int(inicial)

def acumuladores_tipo_envio(tipo_envio):
    global ccs, ccc, cce
    if 0 <= tipo_envio <= 2:
        ccs += 1
    elif 3 <= tipo_envio <= 4:
        ccc += 1
    else:
        cce += 1

def obtener_tipo_carta_mayor_envios():
    global ccs, cce, ccc
    if ccs >= cce and ccs >= ccc:
        return "Carta Simple"
    elif cce >= ccs and cce >= ccc:
        return "Carta Expresa"
    else:
        return "Carta Certificada"

def leer_txt(archivo_txt):
    return open(archivo_txt, "r", encoding="utf-8")

def procesar_linea(linea, control, primer_cp, flag_primer_cp, menimp, mencp, cont_buenos_aires, final_buenos_aires):
    global ccs, ccc, cce
    cp = obtener_cp(linea)
    provincia = obtener_provincia(cp)
    destino = identificar_destino(cp)
    direccion = identificar_direccion(linea)
    tipo_envio = identificar_tipo_envio(linea)
    tipo_pago = identificar_tipo_pago(linea)

    inicial = configurar_tipo_envio(tipo_envio)
    if destino != "Argentina":
        inicial = configurar_envios_internacionales(destino, cp, inicial)
    final = configurar_forma_pago(tipo_pago, inicial)

    if control.lower() == "hard control":
        direccion_valida = validar_direccion(direccion)
        if direccion_valida:
            cedvalid = 1
            cedinvalid = 0
            imp_acu_total = final
            acumuladores_tipo_envio(tipo_envio)
            if provincia == "Buenos Aires":
                final_buenos_aires += final
                cont_buenos_aires += 1
        else:
            cedvalid = 0
            cedinvalid = 1
            imp_acu_total = 0
    else:
        cedvalid = 1
        cedinvalid = 0
        imp_acu_total = final
        acumuladores_tipo_envio(tipo_envio)
        if provincia == "Buenos Aires":
            final_buenos_aires += final
            cont_buenos_aires += 1

    if flag_primer_cp:
        primer_cp = cp
        flag_primer_cp = False

    if destino == "Brasil":
        if menimp is None or final < menimp:
            menimp = final
            mencp = cp

    return (cedvalid, cedinvalid, imp_acu_total, primer_cp, flag_primer_cp, menimp, mencp, final_buenos_aires, cont_buenos_aires)

def calcular_resultados(cont_total_envios_ext, cont_total_envios, cont_buenos_aires, final_buenos_aires):
    porc = int((cont_total_envios_ext * 100) / cont_total_envios) if cont_total_envios else 0
    prom = int(final_buenos_aires / cont_buenos_aires) if cont_buenos_aires else 0
    tipo_mayor = obtener_tipo_carta_mayor_envios()
    return porc, prom, tipo_mayor

def mostrar_resultados(control, cedvalid, cedinvalid, imp_acu_total, ccs, ccc, cce, tipo_mayor, primer_cp, cant_primer_cp, menimp, mencp, porc, prom):
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

def init():
    archivo = leer_txt("envios25.txt")
    control = ""
    primer_cp = ""
    menimp = None
    mencp = ""
    final_buenos_aires = 0
    cont_buenos_aires = 0
    cant_primer_cp = 0
    cedvalid = 0
    cedinvalid = 0
    imp_acu_total = 0
    cont_total_envios_ext = 0
    cont_total_envios = 0
    flag_control = False
    flag_primer_cp = False

    for linea in archivo:
        linea = linea.replace("\n", "")
        if not flag_control:
            control = identificar_control(linea)
            flag_control = True
            flag_primer_cp = True
            continue

        (validos, invalidos, imp_acum, primer_cp, flag_primer_cp, menor_imp, menor_cp, final_ba, cont_ba) = procesar_linea(
            linea, control, primer_cp, flag_primer_cp, menimp, mencp, cont_buenos_aires, final_buenos_aires
        )

        cedvalid += validos
        cedinvalid += invalidos
        imp_acu_total += imp_acum
        final_buenos_aires = final_ba
        cont_buenos_aires = cont_ba
        menimp = menor_imp
        mencp = menor_cp
        cont_total_envios += 1
        if identificar_destino(obtener_cp(linea)) != "Argentina":
            cont_total_envios_ext += 1

    porc, prom, tipo_mayor = calcular_resultados(cont_total_envios_ext, cont_total_envios, cont_buenos_aires, final_buenos_aires)

    mostrar_resultados(control, cedvalid, cedinvalid, imp_acu_total, ccs, ccc, cce, tipo_mayor, primer_cp, cant_primer_cp, menimp, mencp, porc, prom)


if __name__ == '__main__':
    init()


