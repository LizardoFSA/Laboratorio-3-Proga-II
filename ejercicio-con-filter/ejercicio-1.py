# 1. Filtrar números pares de [1-10]
nums_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, nums_base))
print(f"1. Pares: {pares}\n")