# Observatorio meteorologico
# Ingresar cuatro valores de temperatura (valores enteros)
"""Requerimientos:
    a) promedio de temperatura diaria
    b) temperatura máxima
    c) temperatura mínima
    d) informar con mensaje si alguna de las temperaturas supera a la temperatura promedio
"""

temperatura1 = int(input("Ingrese la temperatura: "))
temperatura2 = int(input("Ingrese la temperatura: "))
temperatura3 = int(input("Ingrese la temperatura: "))
temperatura4 = int(input("Ingrese la temperatura: "))

temperatura_promedio = (temperatura1 + temperatura2 + temperatura3 + temperatura4) / 4

temperatura_maxima = max(temperatura1,temperatura2, temperatura3, temperatura4)

temperatura_minima = min(temperatura1, temperatura2, temperatura3, temperatura4)

supera_promedio = False
if temperatura1 > temperatura_promedio or temperatura2 > temperatura_promedio or temperatura3 > temperatura_promedio or temperatura4 > temperatura_promedio:
    supera_promedio = True


print(f"Promedio de temperatura diaria: {temperatura_promedio}")
print(f"Temperatura máxima: {temperatura_maxima}")
print(f"Temperatura mínima: {temperatura_minima}")
if supera_promedio:
    print("Algunas de las temperaturas tomadas supero a la promedio")