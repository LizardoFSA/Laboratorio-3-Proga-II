# 3. Clase de cuadrados 1-10 (sin iter) con método get_lista
class CuadradosLista:
    def __init__(self, max_num):
        self.max_num = max_num
    
    def get_lista_completa(self):
        return [i*i for i in range(1, self.max_num + 1)]

print("3. Cuadrados del 1 al 10 (método get_lista):")
cuadrados_obj = CuadradosLista(10)
print(cuadrados_obj.get_lista_completa())
print()
