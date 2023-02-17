from funciones import sumar, primo

def test_sumar():
    assert sumar(2, 4) == 6

def test_primo():
    assert primo(5) == True
    assert primo(7) == True
    assert primo(9) == False