# Mantenimiento informático

# Requerimientos:
"""
Ingresar 3 equpos informáticos (PC):
    1. Número de identificación (ID) de PC
    2. Tiempo de reparación (expresado en minutos)
    3. Causa de mantenimiento, problemas:
        1 - Problema de Hardware
        2 - Problema de Software
Requerimientos:
 a. ¿Cuál es el tiempo total de las tareas de mantenimiento?
 b. ¿Cuál es la PC (ID) que tuvo mayor tiempo en tareas de mantenimiento?
 c. Tiempo promedio de tareas de mantenimiento
 d. Informar con un mensaje si todas las pc (ID) que se les realizo mantenimiento tuvieron problemas de hardware
"""

print(f"{'/'*6} Sistema de Mantenimiento Informático {'/'*6}")

equipo1 = (input("\n1ra maquina:\nNúmero de identificación de la PC: "),
           int(input("Tiempo de reparación de la PC: ")),
           int(input("Causa de mantenimiento de la PC:\n1- Problema de Hardware.\n2- Problema de Software.\nIngrese la opción: ")))

equipo2 = (input("\n2da maquina:\nNúmero de identificación de la PC: "),
           int(input("Tiempo de reparación de la PC: ")),
           int(input("Causa de mantenimiento de la PC:\n1- Problema de Hardware.\n2- Problema de Software.\nIngrese la opción: ")))

equipo3 = (input("\n3ra maquina:\nNúmero de identificación de la PC: "),
           int(input("Tiempo de reparación de la PC: ")),
           int(input("Causa de mantenimiento de la PC:\n1- Problema de Hardware.\n2- Problema de Software.\nIngrese la opción: ")))

# Ahora, requerimiento a. tiempo total de las tareas de mantenimiento
tiempo_total = equipo1[1] + equipo2[1] + equipo3[1]
print(f"El tiempo total de las tareas de mantenimiento es de: {tiempo_total} minutos.")
# Requerimiento b. ID de la maquina con más tiempo en tareas de mantenimiento
if equipo1[1] > equipo2[1] and equipo1[1] > equipo3[1]:
    primero = equipo1
elif equipo2[1] > equipo1[1] and equipo2[1] > equipo3[1]:
    primero = equipo2
else:
    primero = equipo3
print(f"El equipo que tuvo mayor tiempo en tareas de mantenimiento es el equipo con ID: {primero[0]} con un tiempo de: {primero[1]}")

# c. tiempo promedio de tareas de mantenimiento
tiempo_promedio = int(tiempo_total) / 3
print(f"El tiempo promedio de las tareas de mantenimiento es de: {'{0:.2f}'.format(tiempo_promedio)}")

# d. mensaje si todas las pc (ID) que se les realizo mantenimiento tuvieron problemas de hardware
if equipo1[2] == 1 and equipo2[2] == 1 and equipo3[2] == 1:
    print("Todas las pc que se realizaron mantenimiento tenian problemas de Hardware.")
else:
    print("Las PC recibieron distintos tipos de mantenimiento.")