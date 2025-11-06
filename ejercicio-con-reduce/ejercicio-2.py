from functools import reduce

# 2. Multiplicar todos los elementos de [2, 3, 4]
nums_5 = [2, 3, 4]
producto_total = reduce(lambda acc, x: acc * x, nums_5)
print(f"2. Producto total: {producto_total}\n")