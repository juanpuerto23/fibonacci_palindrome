"""Cree un programa inspirado en conversor_moneda para hacer la serie de fibonacci"""
m = int(input("Escriba el número de sucesiones en la serie de fibonacci que desee:"))
def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n
for i in range(m):
    print(fibonacci(i))
 