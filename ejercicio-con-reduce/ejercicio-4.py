from functools import reduce

# 4. Concatenar todas las cadenas de ["Hola", ", ", "Mundo", "!"]
cadenas_2 = ["Hola", ", ", "Mundo", "!"]
concatenado = reduce(lambda acc, s: acc + s, cadenas_2)
print(f"4. Cadenas concatenadas: '{concatenado}'\n")