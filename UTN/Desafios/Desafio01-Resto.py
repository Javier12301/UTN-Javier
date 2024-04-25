plataformas = int(input("Plataformas: "))
identificador = int(input("Identificador: "))

# las dos primeras plataformas están fuera de srvicio
r = (identificador%(plataformas-2)) + 2
print(r)

# distintos registrosde propiedad del automor
# numerados con valores del 1 al p [1,p]

# calcular a que registro r -> debemos enviar cada tramite
# conociendo el código postal d númerico del lugra de residencia de quien inicia tramite
