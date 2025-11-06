# 10 primeros números pares
def primeros_pares():
    contador = 0
    num = 0
    while contador < 10:
        yield num
        num += 2
        contador += 1

print("1. Primeros 10 pares:")
for par in primeros_pares():
    print(par, end=' ')
print("\n")


# Números impares de una lista
def impares_de_lista(lista_nums):
    for num in lista_nums:
        if num % 2 != 0:
            yield num

print("2. Impares de [1, 2, 3, 4, 5, 6, 7]:")
for impar in impares_de_lista([1, 2, 3, 4, 5, 6, 7]):
    print(impar, end=' ')
print("\n")


# Clase con __iter__ que genera cuadrados
class Cuadrados:
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        for i in range(1, self.max_num + 1):
            yield i * i

print("3. Cuadrados del 1 al 10: ")
for c in Cuadrados(10):
    print(c, end=' ')
print("\n")


# Serie de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("4. Primeros 10 de Fibonacci:")
for f in fibonacci(10):
    print(f, end=' ')
print("\n")