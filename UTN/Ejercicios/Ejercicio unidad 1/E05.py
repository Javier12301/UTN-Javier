# Programa de conversión de medidas
"""Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:

yardas
pulgadas
centímetros
metros

Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies,  1 pulgada = 2.54 centímetros, 1 metro = 100 centímetros."""

# Primero, definimos los valores
print("Conversor de medidas")
numero_en_pies = float(input("Ingrese una medida dada en pies: "))
print(numero_en_pies,"pies")
# Ecuación pies a yarda
# (1 yarda * x pies) = 3 pies -> (1 yarda * x pies) / (3 pies)
numero_en_yarda = (numero_en_pies)/3
print(numero_en_yarda, "yardas")

# Ecuación a pulgadas -> (12 pulgadas * x pie) / (1pie)
numero_en_pulgadas = (12 * numero_en_pies)
print(numero_en_pulgadas, "pulgadas")

#Ecuación a centimetros -> (1 pulgada) = 2.54 centimetros -> (2.54 cm * x pulgada) / (1 pulgada)
numero_en_centimetros = (2.54 * numero_en_pulgadas)
print(numero_en_centimetros, "cm")
# Ecuación a metros -> 1 metro = 100 cm -> (1m * x centimetros) / (100)
numero_en_metros = (numero_en_centimetros)/(100)
print(numero_en_metros, "m")