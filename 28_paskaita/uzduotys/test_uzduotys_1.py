import pytest
from uzduotys_1 import skaiciu_suma, vidurkis, zodziu_skaicius, unikalios_reiksmes

# 1

@pytest.fixture
def skaiciu_uzpildymas():
    sarasas = [1,2,3,4,5]
    return sarasas


def test_skaiciu_suma(skaiciu_uzpildymas):
    assert skaiciu_suma(skaiciu_uzpildymas) == 15

# 2

@pytest.fixture
def skirtingi_sarasai1():
    sarasas = [1,2,3,4,5,6,7]
    return sarasas
@pytest.fixture
def skirtingi_sarasai2():
    sarasas = [10,20,30,40,50]
    return sarasas
@pytest.fixture
def skirtingi_sarasai3():
    sarasas = [0.1, 0.5, 0.8, 0.7]
    return sarasas

def test_vidurkis(skirtingi_sarasai1, skirtingi_sarasai2, skirtingi_sarasai3):
    assert vidurkis(skirtingi_sarasai1) == sum(skirtingi_sarasai1)/len(skirtingi_sarasai1)
    assert vidurkis(skirtingi_sarasai2) == sum(skirtingi_sarasai2)/len(skirtingi_sarasai2)
    assert vidurkis([1,2,'p']) == 'klaida'
    assert vidurkis(skirtingi_sarasai3) == sum(skirtingi_sarasai3)/len(skirtingi_sarasai3)

# 3

@pytest.fixture
def tekstas():
    tekstas = 'Siandien jau penktadienis, beveik savaitgalis'
    return tekstas

@pytest.fixture
def tekstas1():
    tekstas1 = 'Savaitgali zadamas pagaliau siltesnis oras, negu siandien'
    return tekstas1


def test_zodziu_skaicius(tekstas, tekstas1):
    tiketinas_rezultatas = zodziu_skaicius(tekstas)
    assert tiketinas_rezultatas == 5
    tiketinas_rezultatas1 = zodziu_skaicius(tekstas1)
    assert tiketinas_rezultatas1 == 7

# 4 
def unikalios_reiksmes(skaiciu_uzpildymas):
    tiketinas_rezultatas = unikalios_reiksmes(skaiciu_uzpildymas)
    assert tiketinas_rezultatas == [1,2,3,4,5]