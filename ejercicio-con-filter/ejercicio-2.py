# 2. Filtrar palabras que empiezan con "p"
palabras_3 = ["perro", "gato", "pato", "hamster"]
con_p = list(filter(lambda p: p.startswith('p'), palabras_3))
print(f"2. Palabras con 'p': {con_p}\n")