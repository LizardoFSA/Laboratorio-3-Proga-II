# 4. Filtrar números impares de [1-10]
nums_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = list(filter(lambda x: x % 2 != 0, nums_base))
print(f"4. Impares: {impares}\n")