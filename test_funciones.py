from funciones import sumar, primo, menorlista

def test_sumar():
    assert sumar(2, 4) == 6

def test_primo():
    assert primo(5) == True
    assert primo(7) == True
    assert primo(9) == False
    assert primo(10) == False

def test_menorLista():
    assert menorlista([1, 2, 3, 4]) == 1
    assert menorlista([2, 3, 4, 1]) == 1
    assert menorlista([3, 4, 1, 2]) == 1
    assert menorlista([4, 1, 2, 3]) == 1
