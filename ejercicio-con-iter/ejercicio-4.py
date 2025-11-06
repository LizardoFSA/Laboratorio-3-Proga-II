# 4. Iterador de lista de cadenas en mayúsculas
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