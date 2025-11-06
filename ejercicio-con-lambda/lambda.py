# Lambda que recibe dos números y devuelve el mayor
mayor = lambda x, y: x if x > y else y
print(f"1. Mayor entre 10 y 5: {mayor(10, 5)}\n")

# Lambda que recibe una cadena y devuelve su longitud
longitud = lambda s: len(s)
print(f"2. Longitud de 'Hola': {longitud('Hola')}\n")

# Lambda que recibe una lista y devuelve el primer elemento
primero = lambda lista: lista[0] if lista else None
print(f"3. Primero de [10, 20, 30]: {primero([10, 20, 30])}\n")

# Lambda que recibe un número y devuelve su doble
doble = lambda n: n * 2
print(f"4. Doble de 15: {doble(15)}\n")