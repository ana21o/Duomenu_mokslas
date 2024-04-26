import pytest
from gyvunu_prieglauda import Gyvunas, GyvunuPrieglauda


@pytest.fixture
def prieglaudu_kurimas():
    gyvunas1 = Gyvunas(2015, 'suo', 'Reksas', 20)
    prieglauda1 = GyvunuPrieglauda('Lese')
    prieglauda1.prideti_gyvuna(gyvunas1)
    prieglauda1.prideti_gyvuna(Gyvunas(2020, 'kate', 'Test', None))
    return prieglauda1

def test_gauti_pagal_rusi(prieglaudu_kurimas):
    kates = prieglaudu_kurimas.gauti_pagal_rusi('kate')
    sunys = prieglaudu_kurimas.gauti_pagal_rusi('suo')
    assert sunys == [prieglaudu_kurimas.gyvunai[0]]
    assert len(sunys) == 1
    assert len(prieglaudu_kurimas.gyvunai) == 2
    assert kates == [prieglaudu_kurimas.gyvunai[1]]