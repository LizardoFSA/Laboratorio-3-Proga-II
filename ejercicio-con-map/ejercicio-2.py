# 2. Convertir Celsius [0, 10, 20, 30] a Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"2. Celsius a Fahrenheit: {fahrenheit}\n")