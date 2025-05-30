from calculator import dodawanie,dzielenie,mnozenie,odejmowanie,maksimum, minimum, srednia
def test_dodawanie():
    assert dodawanie(2, 3) == 5
    assert dodawanie(-1, 1) == 0

def test_odejmowanie():
    assert odejmowanie(5, 3) == 2
    assert odejmowanie(1, -1) == 2

def test_mnozenie():
    assert mnozenie(2, 3) == 6
    assert mnozenie(-1, 1) == -1

def test_dzielenie():
    assert dzielenie(6, 3) == 2
    assert dzielenie(1, -1) == -1
    assert dzielenie(1, 0) == "Błąd: dzielenie przez zero!"

def test_maksimum():
    assert maksimum([1,9,3]) == 9
    assert maksimum([-30,-19,0]) == 0
    assert maksimum([-7,49,30,81]) == 81

def test_minimum():
    assert minimum([6,9,1]) == 1
    assert minimum([-3,-8,4]) == -8
    assert minimum([19,29,90,42]) == 19


def test_srednia():
    assert srednia([4,5,6]) == 5
    assert srednia([-7,0,7]) == 0
    assert srednia([-9,-8,-2,-1]) == -5