# 2. Generador de impares 1-20 en clase (con yield) e iterado con for
class Impares:
    def __init__(self, max_num):
        self.max_num = max_num
        
    def __iter__(self):
        for i in range(1, self.max_num + 1):
            if i % 2 != 0:
                yield i

print("2. Impares del 1 al 20 (clase con yield y for):")
for impar in Impares(20):
    print(impar, end=' ')
print("\n")