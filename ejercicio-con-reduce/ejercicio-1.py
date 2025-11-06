from functools import reduce

# 1. Sumar todos los elementos de [5, 10, 15, 20]
nums_4 = [5, 10, 15, 20]
suma_total = reduce(lambda acumulador, elemento: acumulador + elemento, nums_4)
print(f"1. Suma total: {suma_total}\n")