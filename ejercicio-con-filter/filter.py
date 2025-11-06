nums_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares
pares = list(filter(lambda x: x % 2 == 0, nums_base))
print(f"1. Pares: {pares}\n")

# Filtrar palabras que empiezan con "p"
palabras_3 = ["perro", "gato", "pato", "hamster"]
con_p = list(filter(lambda p: p.startswith('p'), palabras_3))
print(f"2. Palabras con 'p': {con_p}\n")

# Filtrar números mayores a 50
nums_3 = [10, 60, 30, 80, 50, 100]
mayores_50 = list(filter(lambda n: n > 50, nums_3))
print(f"3. Números mayores a 50: {mayores_50}\n")

# Filtrar números impares
impares = list(filter(lambda x: x % 2 != 0, nums_base))
print(f"4. Impares: {impares}\n")