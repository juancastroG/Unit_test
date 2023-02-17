def sumar(x, y):
    return x + y

def primo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
