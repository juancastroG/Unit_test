def sumar(x, y):
    return x + y

def primo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def menorlista(lista):
    minimo = lista[0]
    for i in lista:
        if i < minimo:
            minimo = i
