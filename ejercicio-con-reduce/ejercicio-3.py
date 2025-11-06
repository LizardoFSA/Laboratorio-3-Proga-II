from functools import reduce

# 3. Encontrar el número mayor de [7, 3, 9, 1, 5]
nums_6 = [7, 3, 9, 1, 5]
mayor_num = reduce(lambda acc, x: acc if acc > x else x, nums_6)
print(f"3. Número mayor: {mayor_num}\n")