# Lista de números del 1 al 50
lista_1_50 = [i for i in range(1, 51)]
print(f"1. Números 1-50: {lista_1_50}\n")

# Cuadrados de los números pares del 1 al 20
cuadrados_pares_1_20= [i**2 for i in range(1, 21) if i % 2 == 0]
print(f"2. Cuadrados pares 1-20: {cuadrados_pares_1_20}\n")

# Primeras letras de "python", "java", "C++", "ruby"
palabras_base = ["python", "java", "C++", "ruby"]
primeras_letras = [palabra[0] for palabra in palabras_base]
print(f"3. Primeras letras: {primeras_letras}\n")

# Números divisibles por 3 del 1 al 30
divisibles_por_3 = [i for i in range(1, 31) if i % 3 == 0]
print(f"4. Divisibles por 3 (1-30): {divisibles_por_3}\n")