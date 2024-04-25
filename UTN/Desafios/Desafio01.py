#Autor: Javier Ramírez
# REQUERIMIENTOS
# Desarrollar un programa que:
 #1. permita cargar un número entero que representa la cantidad de segundos de algun evento cualquiera.
 #2. El programa tiene que convertir esa cantidad de segundos a cantidad de horas, minutos y segundos que transcurrieron
#Ejemplo:
#Si la cantidad de segundos ingresada es 4452 se debe mostrar un informe que el tiempo transcurrido fue: 1 hora, 14 minutos y 12 segundos
# 4452

# La conversión solo se muestra si la cantidad de horas totales es menor o giaul a 24.
 # SI LA CANTIDAD ES MAYOR A 24, EL PROGRAMA MOSTRARÁ UN MENSAJE "Excedido"
#FIN REQUERIMIENTOS

cantidad_segundos = int(input("Ingrese la cantidad de segundos a calcular: "))
# Proceso
horas = cantidad_segundos // 3600
minutos = (cantidad_segundos % 3600) // 60
segundos = cantidad_segundos % 60
# Formatos de string para que salgan como 00:00:00 -> 02:05:24
# {:02d} -> donde d significa decimal y el 0 se rellena si no tiene más digitos el número o sea 2 -> 02 y 2 especifica el ancho o sea el número de caracteres que ocupara la cadena
horas_str = "{:02d}".format(horas)
minutos_str = "{:02d}".format(minutos)
segundos_str = "{:02d}".format(segundos)

if horas <= 24:
    print(f"{horas_str}:{minutos_str}:{segundos_str}")
else:
    print("Excedido")

# Desafio adicional, proceso Inverso
# Tomaremos tres datos, que osn el valor en horas, valor en minutos y valor en segundos transcurrido en un evento dado
# Ejemplo:
# Si los datos ingresados son horas = 4, minutos = 36 y segundos = 8, entonces el resultado debe ser 16568

# Proceso inverso
print("Calculadora del proceso inverso")
horas = int(input("Ingrese la cantidad de horas: "))
if horas <= 24:
    minutos = int(input("Ingrese la cantidad de minutos: "))
    segundos = int(input(("Ingrese la cantidad de segundos: ")))
    # Proceso
    # hora * 3600sg/(1h) + minuto * 60sg/(1min) + 12sg -> lo que vamos a hacer es transformar toda las unidades en segundos
    # y luego sumarlo cuando las unidades sean segundos, de esta manera obtenemos el resultado del proceso inverso
    segundos_totales = (horas * 3600) + (minutos * 60) + segundos
    horas_str = "{:02d}".format(horas)
    minutos_str = "{:02d}".format(minutos)
    segundos_str = "{:02d}".format(segundos)
    print(f"{horas_str}:{minutos_str}:{segundos_str} es: {segundos_totales} sg")
else:
    print("Excedido")