import pytest
from receptai.receptu_valdymas import Receptas, ReceptuValdymas

@pytest.fixture
def receptu_valdymas():
    valdymas = ReceptuValdymas()
    valdymas.prideti_recepta(Receptas('Cepelinai', 180, ['bulves', 'mesa']))
    valdymas.prideti_recepta(Receptas('Cezario salotos', 30, []))
    valdymas.prideti_recepta(Receptas('Karbonadas', 45, []))
    return valdymas

def test_gauti_receptus_pagal_laika(receptu_valdymas):
    rezultatas = receptu_valdymas.gauti_receptus_pagal_laika(30)
    pavadinimai = [receptas.pavadinimas for receptas in rezultatas]
    assert pavadinimai == ['Cezario salotos']
    assert 'Karbonadas' not in pavadinimai

def test_atrinkti_pagal_ingredientus(receptu_valdymas):
    tikimas_rezultatas = receptu_valdymas.receptai[0]
    assert receptu_valdymas.atrinkti_pagal_ingredientus('bulves') == [tikimas_rezultatas]


# 1

def test_pasalinti_recepta(receptu_valdymas):
    receptu_valdymas.pasalinti_recepta('Karbonadas')
    assert 'Karbonadas' not in [receptas.pavadinimas for receptas in receptu_valdymas.receptai]


# 2

def test_gauti_receptus_pagal_zodi(receptu_valdymas):
    rezultatas = receptu_valdymas.gauti_receptus_pagal_zodi('cepelinai')
    assert rezultatas == ['Cepelinai']

    rezultatas = receptu_valdymas.gauti_receptus_pagal_zodi('salotos')
    assert rezultatas == ['Cezario salotos']

    rezultatas = receptu_valdymas.gauti_receptus_pagal_zodi('pica')
    assert rezultatas == []
 
# 3

def test_gauti_bendra_ruosimo_laika(receptu_valdymas):
    assert receptu_valdymas.gauti_bendra_ruosimo_laika() == 255

# 4

def test_isvalyti_receptus(receptu_valdymas):
    receptu_valdymas.isvalyti_receptus()
    assert receptu_valdymas.receptai == []


