from functools import reduce

# Sumar todos los elementos
nums_4 = [5, 10, 15, 20]
suma_total = reduce(lambda acumulador, elemento: acumulador + elemento, nums_4)
print(f"1. Suma total: {suma_total}\n")

# Multiplicar todos los elementos
nums_5 = [2, 3, 4]
producto_total = reduce(lambda acc, x: acc * x, nums_5)
print(f"2. Producto total: {producto_total}\n")

# Encontrar el número mayor
nums_6 = [7, 3, 9, 1, 5]
mayor_num = reduce(lambda acc, x: acc if acc > x else x, nums_6)
print(f"3. Número mayor: {mayor_num}\n")

# Concatenar todas las cadenas
cadenas_2 = ["Hola", " ", "Mundo", "!"]
concatenado = reduce(lambda acc, s: acc + s, cadenas_2)
print(f"4. Cadena concatenada: {concatenado}\n")