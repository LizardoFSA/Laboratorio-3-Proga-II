# Contador del 10 al 15 con iter y next
print("1. Contador 10-15 con iter() y next():")
contador = iter(range(10, 16))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print()


# Generador de impares 1-20 en clase e iterado con for
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


# Clase de cuadrados 1-10 (sin iter) con método get_lista()
class CuadradosLista:
    def __init__(self, max_num):
        self.max_num = max_num
    
    def get_lista_completa(self):
        return [i*i for i in range(1, self.max_num + 1)]

print("3. Cuadrados del 1 al 10 (método get_lista):")
cuadrados_obj = CuadradosLista(10)
print(cuadrados_obj.get_lista_completa())
print()


# Iterador de lista de cadenas en mayúsculas
class IteradorMayusculas:
    def __init__(self, lista_cadenas):
        self.iterador_interno = iter(lista_cadenas)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        siguiente = next(self.iterador_interno)
        return siguiente.upper()

print("4. Iterador de mayúsculas:")
cadenas = ["hola", "mundo", "python"]
iterador_mayus = IteradorMayusculas(cadenas)
try:
    print(next(iterador_mayus))
    print(next(iterador_mayus))
    print(next(iterador_mayus))
    print(next(iterador_mayus))
except StopIteration:
    print("Fin de la iteración.")
print()