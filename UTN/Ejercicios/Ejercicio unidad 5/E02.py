# Elecciones presidenciales

# Elección de presidente y vicepresidente se eligen de acuerdo a la siguientes reglas:
"""
    1. Resulta electo la FÓRMULA QUE OBTENGA 45% de votos afirmativos
        a. aquella que obtiene 40% y que tiene una diferencia mayor de diez puntos porcentuales
        respecto al total de votos sobre la formula que le sigue en número de votos.

    2. Si ninguna formula alcanza esa mayoria y diferencia, se realizará una segunda vuelta dentro de 30 días

    3. En la segunda vuelta participan solo las dos fórmulas más votadas en la primera, resultando electa
    la que obtenga mayor números de votos afirmativos
    """

""" 
    Requerimientos:
    1. desarrollar un programa que permita ingresar los 3 partidos más votados: fórmula (presidente + vice) y cantidad de 
    votos obtenidos.
    
    Determinar:
     a. formula que obtuvo mayor porcentaje
     b. si la formula resulta elegida o requiere segunda vuelta, indicar quienes participan de la segunda vuelta.
"""

# Ingresamos los partidos politicos
partido_politico1 = input("Ingrese los candidatos con el formato (presidente + vice): ")
cantidad_votos1 = int(input("Ingrese la cantidad de votos: "))

partido_politico2 = input("Ingrese los candidatos con el formato (presidente + vice): ")
cantidad_votos2 = int(input("Ingrese la cantidad de votos: "))

partido_politico3 = input("Ingrese los candidatos con el formato (presidente + vice): ")
cantidad_votos3 = int(input("Ingrese la cantidad de votos: "))

# Obtener votos totales:
cantidad_votos_totales = cantidad_votos1 + cantidad_votos2 + cantidad_votos3
# Obtener votos porcentuales para cada partido
votos_porcentual1 = (cantidad_votos1 / cantidad_votos_totales) * 100

votos_porcentual2 = (cantidad_votos2 / cantidad_votos_totales) * 100

votos_porcentual3 = (cantidad_votos3 / cantidad_votos_totales) * 100

# Determinar ganador de los 3
segunda_vuelta_flag = False
if votos_porcentual1 > votos_porcentual2 and votos_porcentual1 > votos_porcentual3:
    primero = partido_politico1
    porcentaje_primero = votos_porcentual1
    if votos_porcentual2 > votos_porcentual3:
        segundo = partido_politico2
        porcentaje_segundo = votos_porcentual2
        tercero = partido_politico3
        porcentaje_tercero = votos_porcentual3
    else:
        segundo = partido_politico3
        porcentaje_segundo = votos_porcentual3
        tercero = partido_politico2
        porcentaje_tercero = votos_porcentual2
elif votos_porcentual2 > votos_porcentual1 and votos_porcentual2 > votos_porcentual3:
    primero = partido_politico2
    porcentaje_primero = votos_porcentual2
    if votos_porcentual1 > votos_porcentual3:
        segundo = partido_politico1
        porcentaje_segundo = votos_porcentual1
        tercero = partido_politico3
        porcentaje_tercero = votos_porcentual3
    else:
        segundo = partido_politico3
        porcentaje_segundo = votos_porcentual3
        tercero = partido_politico1
        porcentaje_tercero = votos_porcentual1
else:
    primero = partido_politico3
    porcentaje_primero = votos_porcentual3
    if votos_porcentual2 > votos_porcentual1:
        segundo = partido_politico2
        porcentaje_segundo = votos_porcentual2
        tercero = partido_politico1
        porcentaje_tercero = votos_porcentual1
    else:
        segundo = partido_politico1
        porcentaje_segundo = votos_porcentual1
        tercero = partido_politico2
        porcentaje_tercero = votos_porcentual2

# Una vez determinado, verificar quien es el ganador
# Sabemos que el primero debe obtener 45% votos y el que obtuvo 40
if porcentaje_primero >= 45:
    print(f"El candidato {primero} es electo por tener más del 45%, gano con un total de: {'{0:.2f}'.format(porcentaje_primero)}%")
elif porcentaje_primero >= 40 and (porcentaje_primero - porcentaje_segundo) > 10:
    print(f"El candidato {primero} es electo por tener {'{0:.2f}'.format(porcentaje_primero)}% y tener una diferencia mayor de 10 puntos porcentuales con el segundo: {porcentaje_segundo}")
else:
    print("Como no se alcanzaron los requisitos establecidos, se deberá ir a una segunda vuelta\nParticiparan de la segunda vuelta los siguientes candidatos:")
    print(f"El candidato a presidente y su vicepresidente: {primero} que obtuvo un porcentaje de votos de: {'{0:.2f}'.format(porcentaje_primero)}%")
    print(f"El candidato a presidente y su vicepresidente: {segundo} que obtuvo un porcentaje de votos de: {'{0:.2f}'.format(porcentaje_segundo)}%")

print(f"\n\nEl primer lugar es para {primero} con un porcentaje de votos de {'{0:.2f}'.format(porcentaje_primero)}%")
print(f"El segundo lugar es para {segundo} con un porcentaje de votos de {'{0:.2f}'.format(porcentaje_segundo)}%")
print(f"El tercer lugar es para {tercero} con un porcentaje de votos de {'{0:.2f}'.format(porcentaje_tercero)}%")



