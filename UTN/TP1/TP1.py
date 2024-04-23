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



#INTRODUCCIÓN - # N: Número o Dígito del 0 al 9 , # L: Significa Letra
 # País - Formato CP:
  #Argentina: LNNNNLLL
   #Ejemplo jesus maria: “C5224JMD”.
   #CP podría ser algo como esto: “C5224JMD”.
    # Aquí, “C” representa a la provincia de Córdoba,
    # “5224” representa a la ciudad de Jesús María,
    # y “JMD” presentar un frente de manzana, paraje o casilla de correo específico en esa ciudad.
  #Bolivia: NNNN

  #Brasil: NNNNN-NNN

  #Chile: NNNNNNN

  #Paraguay NNNNNN

  #Uruguay: NNNNN

# El correo central Argentino tiene *ARANCELES* por *Tipo de envio* , *Por peso* y por *destino*
# De acuerdo a las siguientes tablas:

 # ENVIOS NACIONALES (Dentro de la propia Argentina)

#| Tipo de Envío       | Id | Peso (p) en gramos | Precio (en pesos) |
#|---------------------|----|--------------------|-------------------|
#| Carta Simple        | 0  | p < 20             | 1100              |
#| Carta Simple        | 1  | 20 <= p < 150      | 1800              |
#| Carta Simple        | 2  | 150 <= p < 500     | 2450              |
#| Carta Certificada   | 3  | p < 150            | 8300              |
#| Carta Certificada   | 4  | 150 <= p < 500     | 10900             |
#| Carta Expresa       | 5  | p < 150            | 14300             |
#| Carta Expresa       | 6  | 150 <= p < 500     | 17900             |
#|---------------------|----|--------------------|-------------------|

# El ID lo usaremos para identificar nuestros condicionales

#ENVIOS INTERNACIONALES (Fuera de la Argentina)

#| País destino                          | Precio (en pesos) |
#|---------------------------------------|-------------------|
#| Bolivia, Paraguay, Uruguay(Montevideo)| +20%              |
#| Chile, Uruguay (no Montevideo)        | +25%              |
#| Brasil (regiones 8 y 9)               | +20%              |
#| Brasil (regiones 0, 1, 2 y 3)         | +25%              |
#| Brasil (regiones 4, 5, 6 y 7)         | +30%              |
#| Otros países                          | +50%              |
#|---------------------------------------|-------------------|

# El porcentaje sería un extra que hay que pagar
# 20% -> 1.20 para aumentar 20%

# REQUERIMIENTOS
# DEBEMOS DESARROLLAR UN PROGRAMA QUE GESTIONE DATOS DE UN ÚNICO ENVIO
# EL CUAL FUE RECIBIDO PARA SU DESPACHO EN VENTANILLA DEL CORREO ARGENTINO
# LOS DATOS A CARGAR PARA EL ENVIO SON:
 # *El codigo postal (CP) del destino: una cadena de caracteres
 # *Dirección física del destino: una cadena de caracteres (sin validación ni formato especial) solo indicando dirección concreta de entrega
 # *Tipo de evnío: un número entre 0 y 6 que indica algunos de los siete tipos posibles (Columna "id") en la tabla de tipos de envio
#  - se asume que el usuario cargará estrictamente alguno de esos dígitos y ningun otro.
 # *Forma de pago: un número entero que indica los dos siguientes tipos de pago: 1: efectivo, 2: tarjeta de crédito
# - se asume que el usuario cargará estrictamente alguno de esos dígitos, y ningún otro

# LUEGO DE CARGAR LOS DATOS del único envio a procesar: el programa nos debe permitir simular la emisión del ticket
# de cobro en base a los siguientes items:

# 1. Indicar nombre del pais de destino -> cumplir formato de los CP de los paises
 #  en este TP (Argentina y sus paises vecinos) -> si el CP no cumpliera con ninguno de esos formatos
 #  Debemos informar que el pais es "Otro" -> Podemos utilizar un switch
 # IF(Argentina) - ELIF(Bolivia, Paraguay, Chile, Brasil) - ELSE (Otro)
 
# 2. Si el envío se realiza hacia un DESTINO (Provincia) DENTRO DE ARGENTINA, -SI ES IF(ARGENTINA)-
# * Debemos Indicar Nombre de la Provincia hacía la que va el envío (Para hacerlo, debemos identificar cada provincia según estándar ISO 3166-2:AR)
# https://academia-lab.com/enciclopedia/iso-3166-2ar/#:~:text=ISO%203166-2%3AAR%20es%20la%20entrada%20para%20Argentina%20en,de%20todos%20los%20pa%C3%ADses%20codificados%20en%20ISO%203166-1.
# * Si el envío no es al INTERIOR DE ARGENTINA, entonces mostrar la cadena "No aplica" (LIMITROFES)?¿

# 3. indicar el importe  a pagar por el envio(usar las tablas 2 y 3 sobre envios nacionales y no nacionales) usar valores enteros redondeando para arriba el valor. 
# se podria definir los valores de la tabla 2 y 3 y linkearlos con el importe a pagar.

# 4. aplicar un descuento de 10% si el pago se realiza con EFECTIVO al importe del punto 3, indicar por separado el importe final a pagar por el envio.
# (imprimir ambos valores incluso sean iguales, TRUNCAR los decimales)

#TABLA 1 - FORMATO CÓDIGO POSTALES


# DEFINIR TUPLA DE TIPOS DE ENVIO
#tipos_envio[i] -> 0 sería nuestra ID, 
#tipos_envio[1] -> 1 sería nuestra ID



#| Tipo de Envío       | Id | Peso (p) en gramos | Precio (en pesos) |
#|---------------------|----|--------------------|-------------------|
#| Carta Simple        | 0  | p < 20             | 1100              |
#| Carta Simple        | 1  | 20 <= p < 150      | 1800              |
#| Carta Simple        | 2  | 150 <= p < 500     | 2450              |
#| Carta Certificada   | 3  | p < 150            | 8300              |
#| Carta Certificada   | 4  | 150 <= p < 500     | 10900             |
#| Carta Expresa       | 5  | p < 150            | 14300             |
#| Carta Expresa       | 6  | 150 <= p < 500     | 17900             |
#|---------------------|----|--------------------|-------------------|

# DEFINIR VARIABLES/TUPLAS
# CP - patrones para definir pais destino
# LNNNNLLL - ARGENTINA
patron_argentina = r'^[A-Za-z][0-9]{4}[A-Za-z]{3}'
# NNNN - Bolivia
patron_bolivia = r'^[0-9]{4}'


tipos_envio = (1100, 1800, 2450, 8300, 10900, 14300, 17900)


# CARGA DE DATOS OBLIGATORIAS
cp = input("Ingrese el código postal del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
direccion = input("Dirección del lugar de destino: ")
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

# DESPUES DE LA CARGA DE DATOS
#[0, 6]
if tipo >= 0 and tipo <= 6:
    inicial = tipos_envio[tipo]
else :
    print("ingrese una ID Correcta")

# PROCESAR DATOS

# DESPUES DEL PROCESAMIENTO DE LOS DATOS
destino = (input("ingrese el pais de destino")) #Esto lo determinamos a partir del código postal
provincia = "cordoba" # Esto lo podemos determinar también por el código postal
inicial = 1200 # Lo calculamos a partir del TIPO DE ENVIO y el PESO (cuanto pesa el envio)
final = inicial # LO CALCULAMOS A PARTIR DEL IMPORTE INICIAL Y LA FORMA DE PAGO (EFECTIVO O TARJETA)
descuento = inicial * 0.10 # 10% descuento
precio_efectivo = inicial - descuento

#--------------------------------------------------------------
# SALIDA DEL RESULTADO
print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)


