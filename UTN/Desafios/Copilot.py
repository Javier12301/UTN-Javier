def convertir_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60
    if horas <= 24:
        return f"{horas}:{minutos}:{segundos}"
    else:
        return "Excedido"

def convertir_a_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

def main():
    # Prueba de la función convertir_segundos
    segundos = int(input("Ingrese la cantidad de segundos: "))
    resultado = convertir_segundos(segundos)
    print(f"El tiempo transcurrido es: {resultado}")

    # Prueba de la función convertir_a_segundos
    horas = int(input("Ingrese la cantidad de horas: "))
    minutos = int(input("Ingrese la cantidad de minutos: "))
    segundos = int(input("Ingrese la cantidad de segundos: "))
    resultado = convertir_a_segundos(horas, minutos, segundos)
    print(f"La cantidad total de segundos es: {resultado}")

if __name__ == "__main__":
    main()
