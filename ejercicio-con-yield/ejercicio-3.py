# 3. Clase con __iter__ que genera cuadrados
class Cuadrados:
    """Genera los cuadrados del 1 al 10 usando yield en __iter__."""
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        for i in range(1, self.max_num + 1):
            yield i * i

print("3. Cuadrados del 1 al 10 (con clase y yield):")
for c in Cuadrados(10):
    print(c, end=' ')
print("\n")