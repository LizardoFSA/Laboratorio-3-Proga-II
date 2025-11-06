# Multiplicar por 10 la lista
nums_1 = [1, 2, 3, 4, 5]
multiplicados = list(map(lambda x: x * 10, nums_1))
print(f"1. Multiplicados por 10: {multiplicados}\n")

# Convertir Celsius a Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"2. Celsius a Fahrenheit: {fahrenheit}\n")

# Obtener longitudes de palabras
palabras_2 = ["uno", "dos", "tres"]
longitudes = list(map(len, palabras_2)) 
print(f"3. Longitudes de palabras: {longitudes}\n")

# Cuadrado de cada número
nums_2 = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, nums_2))
print(f"4. Cuadrados: {cuadrados}\n")
