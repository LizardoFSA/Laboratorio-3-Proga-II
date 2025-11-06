# 3. Lambda que recibe una lista y devuelve el primer elemento
primero = lambda lista: lista[0] if lista else None
print(f"3. Primero de [10, 20, 30]: {primero([10, 20, 30])}\n")