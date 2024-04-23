# últimos dígitos
"""
¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero?
¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado,
y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado)
[Ayuda: ¿cuáles son los posibles restos que se obtienen de dividir un número cualquiera por 10?]
"""

# Podemos obtener el último dígito al obtener el resto de la división de 10
# Si hacemos una división de cualquier número por 10 obtendremos el primer último digito
# Si hacemos con cien, obtendremos los dos últimos digitos

print("Obtener los dos últimos digitos")
num_int = int(input("Ingrese un número entero: "))

print(f"Número entero ingresado: {num_int}")
print(f"* Último digito: {num_int % 10}")
print(f"* Dos últimos digitos: {num_int % 100}")