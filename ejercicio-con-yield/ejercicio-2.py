# 2. Números impares de una lista
def impares_de_lista(lista_nums):
    """Devuelve solo los números impares de una lista."""
    for num in lista_nums:
        if num % 2 != 0:
            yield num

print("2. Impares de [1, 2, 3, 4, 5, 6, 7]:")
for impar in impares_de_lista([1, 2, 3, 4, 5, 6, 7]):
    print(impar, end=' ')
print("\n")