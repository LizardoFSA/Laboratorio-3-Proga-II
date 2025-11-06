# 1. 10 primeros números pares
def primeros_pares():
    """Genera los primeros 10 números pares."""
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