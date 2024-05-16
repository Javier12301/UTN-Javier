"""
______datos______:
carga por teclado:
cp_destino
direccion fisica: (paises, provincias)
tipo de envio: (tabla 2)
forma de pago: (1:efectivo(10%), 2:trajeta de credito)

______procesos______:
1) determinar los paises de destino
2) determinar la provincia(si el envio es realizado en argentina)
3) calcular importe inicial a pagar_____tipo envio [inicial]
4) aplicar ajuste segun el pais de destino [final]

_____salidas______:
imprimir (print):
1) pais del destino [destino]
2) provincia destino [provincia]
3) importe inicial [inicial]
4) importe con ajuste aplicado(en caso de que el pago sea en efectivo) [final]

"""
cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

paises = {
    "Argentina": ["LNNNNLLL"],
    "Bolivia": ["NNNN"],
    "Brasil": ["NNNNN-NNN"],
    "Chile": ["NNNNNNN"],
    "Paraguay": ["NNNNNN"],
    "Uruguay": ["NNNNN"]
}

destino = "otro"
if cp[0] in ("L", "N"):
    if cp in paises["Argentina"]:
        destino = "Argentina"
    elif cp in paises["Bolivia"]:
        destino = "Bolivia"
    elif cp in paises["Brasil"]:
        destino = "Brasil"
    elif cp in paises["Chile"]:
        destino = "Chile"
    elif cp in paises["Paraguay"]:
        destino = "Paraguay"
    elif cp in paises["Uruguay"]:
        destino = "Uruguay"

provincia = "No aplica"
if destino == "Argentina":
     standar_iso = {
         "Buenos Aires": ["A"],
         "Catamarca": ["K"],
         "Chaco": ["H"],
         "Chubut": ["U"],
         "Córdoba": ["X"],
         "Corrientes": ["W"],
         "Entre Ríos": ["E"],
         "Formosa": ["P"],
         "Jujuy": ["Y"],
         "La Pampa": ["L"],
         "La Rioja": ["F"],
         "Mendoza": ["M"],
         "Misiones": ["N"],
         "Neuquén": ["Q"],
         "Río Negro": ["R"],
         "Salta": ["O"],
         "San Juan": ["J"],
         "San Luis": ["D"],
         "Santa Cruz": ["Z"],
         "Santa Fe": ["S"],
         "Santiago del Estero": ["G"],
         "Tierra del Fuego": ["V"],
         "Tucumán": ["T"]
     }
     letra_de_provincia = cp[0]
     if letra_de_provincia in standar_iso["Buenos Aires"]:
         provincia = "Buenos aires"
     elif letra_de_provincia in standar_iso["Catamarca"]:
        provincia = "Catamarca"
     elif letra_de_provincia in standar_iso["Chaco"]:
         provincia = "Chaco"
     elif letra_de_provincia in standar_iso["Chubut"]:
         provincia = "Chubut"
     elif letra_de_provincia in standar_iso["Cordoba"]:
         provincia = "Cordoba"
     elif letra_de_provincia in standar_iso["Corrientes"]:
         provincia = "Corrientes"
     elif letra_de_provincia in standar_iso["Entre Ríos"]:
         provincia = "Entre Ríos"
     elif letra_de_provincia in standar_iso["Formosa"]:
         provincia = "Formosa"
     elif letra_de_provincia in standar_iso["Jujuy"]:
         provincia = "Jujuy"
     elif letra_de_provincia in standar_iso["La Pampa"]:
         provincia = "La Pampa"
     elif letra_de_provincia in standar_iso["La Rioja"]:
         provincia = "La Rioja"
     elif letra_de_provincia in standar_iso["Mendoza"]:
         provincia = "Mendoza"
     elif letra_de_provincia in standar_iso["Misiones"]:
         provincia = "Misiones"
     elif letra_de_provincia in standar_iso["Neuquén"]:
         provincia = "Neuquén"
     elif letra_de_provincia in standar_iso["Río Negro"]:
         provincia = "Río Negro"
     elif letra_de_provincia in standar_iso["Salta"]:
         provincia = "Salta"
     elif letra_de_provincia in standar_iso["San Juan"]:
         provincia = "San Juan"
     elif letra_de_provincia in standar_iso["San Luis"]:
         provincia = "San Luis"
     elif letra_de_provincia in standar_iso["Santa Cruz"]:
         provincia = "Santa Cruz"
     elif letra_de_provincia in standar_iso["Santa Fe"]:
         provincia = "Santa fe"
     elif letra_de_provincia in standar_iso["Santiago del Estero"]:
         provincia = "Santiago del Estero"
     elif letra_de_provincia in standar_iso["Tierra del Fuego"]:
         provincia = "Tierra del Fuego"
     elif letra_de_provincia in standar_iso["Tucumán"]:
         provincia = "Tucumán"

precios = {
    "Carta simple": {0: 1100, 1: 1800, 2: 2450},
    "Carta certificada": {3: 8300, 4: 10900},
    "Carta expresada": {5: 14300, 6: 17900}
}

inicial = None

if tipo in range (7):
    if tipo in precios ["Carta simple"]:
        inicial = precios["Carta simple"][tipo]
    elif tipo in precios ["Carta certificada"]:
        inicial = precios["Carta certificada"][tipo]
    elif tipo in precios["Carta expresada"]:
        inicial = precios["Carta expresada"][tipo]

if destino != "otro":
    ajustes = {
        "Bolivia": 0.2,
        "Paraguay": 0.2,
        "Uruguay": 0.2,
        "Chile": 0.25,
        "Brasil": {8: 0.2, 9: 0.2, 0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25, 4: 0.3, 5: 0.3, 6: 0.3, 7: 0.3}


    }

    ajuste = ajustes.get(destino, 0.5)
    inicial *= ajuste

if pago == 1:
    final = int(inicial * 0.9)
else:
    final = inicial

print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", int(inicial))
print("Importe final a pagar:", int(final))










