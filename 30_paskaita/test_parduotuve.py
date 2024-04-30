import pytest
from parduotuve import Preke, Parduotuve
@pytest.fixture
def sukurti_parduotuve():
    parduotuve = Parduotuve()
    parduotuve.prideti_preke(Preke('Stalas', 150, 20))
    parduotuve.prideti_preke(Preke('Lempa', 35, 40))
    parduotuve.prideti_preke(Preke('Kede', 50, 12))
    parduotuve.prideti_preke(Preke('Sofa', 600, 25))
    return parduotuve
   

def test_gauti_preke_pagal_index(sukurti_parduotuve):
    preke = sukurti_parduotuve.gauti_preke_pagal_index(0)
    assert preke.pavadinimas == 'Stalas'
    assert preke.kaina == 150  
    assert preke.kiekis == 20 

def gauti_preke_pagal_index1(sukurti_parduotuve):
    preke = sukurti_parduotuve.gauti_preke_pagal_index(1)
    assert preke.pavadinimas == 'Lempa'
    assert preke.kaina == 35
    assert preke.kiekis == 40


def test_istrinti_preke(sukurti_parduotuve):
    preke_pries_istrinama = sukurti_parduotuve.gauti_preke_pagal_index(0)
    assert preke_pries_istrinama is not None
    sukurti_parduotuve.istrinti_preke(0)
    preke_po_istrinimo = sukurti_parduotuve.gauti_preke_pagal_index(0)
    assert preke_po_istrinimo.pavadinimas == 'Lempa'

def test_rikiuoti_pagal_savybe(sukurti_parduotuve):
    # pavadinimas = sukurti_parduotuve.rikiuoti_pagal_savybe('pavadinimas')
    # assert pavadinimas == sorted([preke.__str__() for preke in sukurti_parduotuve.prekes], key=lambda preke: preke['pavadinimas'])
    surikiuotos_prekes = sukurti_parduotuve.rikiuoti_pagal_savybe('pavadinimas')
    tiketinas_rezultatas = ['Kede | 50.0 | 12', 'Lempa | 35.0 | 40', 'Sofa | 600.0 | 25', 'Stalas | 150.0 | 20']
    assert surikiuotos_prekes == tiketinas_rezultatas
    surikiuotos_prekes = sukurti_parduotuve.rikiuoti_pagal_savybe('kaina')
    tiketinas_rezultatas = ['Lempa | 35.0 | 40', 'Kede | 50.0 | 12', 'Stalas | 150.0 | 20', 'Sofa | 600.0 | 25']
    assert surikiuotos_prekes == tiketinas_rezultatas

def test_atnaujinti_preke_sekmingai(sukurti_parduotuve):
    nauja_preke = Preke('Stalas', 200, 30)
    sukurti_parduotuve.atnaujinti_preke(0, nauja_preke)
    atnaujinta_preke = sukurti_parduotuve.gauti_preke_pagal_index(0)
    assert atnaujinta_preke is not None
    assert atnaujinta_preke.pavadinimas == nauja_preke.pavadinimas
    assert atnaujinta_preke.kaina == nauja_preke.kaina
    assert atnaujinta_preke.kiekis == nauja_preke.kiekis

def test_atnaujinti_preke_neegzistuoja(sukurti_parduotuve):
    neegzistuojanti_preke = Preke('Spinta', 100, 10)
    sukurti_parduotuve.atnaujinti_preke(4, neegzistuojanti_preke)
    atnaujinti_preke = sukurti_parduotuve.gauti_preke_pagal_index(4)
    assert atnaujinti_preke is None