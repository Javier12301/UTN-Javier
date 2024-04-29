import re
# INTEGRANTES
"""
Da costa Bonetti Nicolás - 41.203.867 - 414563 - 1K13

Ramirez Javier - 44.608.055 - 414638 - 1K13

Villanueva Tomás - 46.033.827 - 405514 - 1K13

Ambrosino Ignacio - 46.848.058 - 414663 - 1K13

Molina Jonathan -  87298 - 1K13
"""
# Sistema Simple de Gestión de Envíos por Correo

# Entrada de datos
cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

# Variables finales
destino = ""
provincia = ""
inicial = 0
final = 0

# Procesamiento
if len(cp) == 8 and cp[0].isalpha and cp[0] != "O" and cp[0] != "I" and cp[1:4].isdigit() and [cp[5:].isalpha]:
      # Detección provincias
      destino = "Argentina"
      if(cp[0] == "C"):
        provincia = "Ciudad Autónoma de Buenos Aires"
      elif(cp[0] == "B"):
        provincia = "Buenos Aires"
      elif(cp[0]== "K"):
        provincia = "Catamarca"
      elif(cp[0] == "H"):
        provincia = "Chaco"
      elif(cp[0] == "U"):
        provincia = "Chubut"
      elif(cp[0] == "X"):
        provincia = "Córdoba"
      elif(cp[0] == "W"):
        provincia = "Corrientes"
      elif(cp[0] == "E"):
        provincia = "Entre Ríos"
      elif(cp[0] == "P"):
        provincia = "Formosa"
      elif(cp[0] == "Y"):
        provincia = "Jujuy"
      elif(cp[0] == "L"):
        provincia = "La Pampa"
      elif(cp[0] == "F"):
        provincia = "La Rioja"
      elif(cp[0] == "M"):
        provincia = "Mendoza"
      elif(cp[0] == "N"):
        provincia = "Misiones"
      elif(cp[0] == "Q"):
       provincia = "Neuquén"
      elif(cp[0] == "R"):
        provincia = "Rio Negro"
      elif(cp[0] == "A"):
        provincia = "Salta"
      elif(cp[0] == "J"):
        provincia = "San Juan"
      elif(cp[0] == "D"):
        provincia = "San Luis"
      elif(cp[0] == "Z"):
        provincia = "Santa Cruz"
      elif(cp[0] == "S"):
        provincia = "Santa Fe"
      elif(cp[0] == "G"):
        provincia = "Santiago del Estero"
      elif(cp[0] == "V"):
        provincia = "Tierra del Fuego"
      elif(cp[0] == "T"):
        provincia = "Tucumán"
elif len(cp) == 4 and cp[:4].isdigit():
  destino = "Bolivia"
  provincia = "No aplica"
  
elif len(cp) == 9 and cp[:4].isdigit() and cp[5] == "-" and cp[6:8].isdigit():
  destino = "Brasil"
  provincia = "No aplica"
  
elif len(cp) == 7 and cp[:6].isdigit():
  destino = "Chile"
  provincia = "No aplica"
  
elif len(cp) == 6 and cp[:5].isdigit():
  destino = "Paraguay"
  provincia = "No aplica"
  
elif len(cp) == 5 and cp[:4].isdigit():
  destino = "Uruguay"
  provincia = "No aplica"
  
else:
  destino = "Otro"
  provincia = "No aplica"
  
# Código de tipo de envio
#[0, 6]
if(tipo >= 0 and tipo <= 6):
    if(tipo == 0):
        inicial = 1100  
    elif(tipo == 1):
        inicial = 1800 
    elif(tipo == 2):
        inicial = 2450
    elif(tipo == 3):
        inicial = 8300
    elif(tipo == 4):
        inicial = 10900
    elif(tipo == 5):
        inicial = 14300    
    elif(tipo == 6):
        inicial = 17900
# Configuración de envios internacionales
if destino == "Bolivia" or destino == "Paraguay":
    # Aumentamos un +20%
    inicial = int(inicial * 1.20)
elif destino == "Uruguay":
    # verificar si es montevideo o no
    if cp[0] == "1":
        # es montevideo
        inicial = int(inicial * 1.20)
    else:
        # no es montevideo -> se aumenta +25%
        inicial = int(inicial * 1.25)
elif destino == "Chile":
    inicial = int(inicial * 1.25)
elif destino == "Brasil":
    # if del 0 al 3 +%25
     if cp[0] == "O" or cp[0] == "1" or cp[0] == "2" or cp[0] == "3":
         inicial = int(inicial * 1.25)
     elif cp[0] == "4" or cp[0] == "5" or cp[0] == "6" or cp[0] == "7":
     # if del 4 al 7 +%30
         inicial = int(inicial * 1.30)
     elif cp[0] == "8" or cp[0] == "9":
         inicial = int(inicial * 1.20)
elif destino == "Otro":
    inicial = int(inicial * 1.50)

# Proceso de forma de pago
# Aplicar descuento 
if pago == 1:
    final = int(inicial * 0.90)
else:
    final = int(inicial)

# Salida
print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)