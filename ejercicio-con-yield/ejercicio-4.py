# 4. Serie de Fibonacci (10 primeros)
def fibonacci(n):
    """Genera los primeros n elementos de la serie Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("4. Primeros 10 de Fibonacci:")
for f in fibonacci(10):
    print(f, end=' ')
print("\n")