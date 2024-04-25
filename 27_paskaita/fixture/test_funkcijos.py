import pytest
import funkcijos as fn

def test_skip():
    savaites_diena = 'sekmadienis'
    if savaites_diena == 'sekmadienis':
        pytest.skip('Praleidziam si testa, nes siandien sekmadienis')  #naudojame, kai norim praleisti
    assert fn.apskaiciuoti_plota(5,4) == 20

@pytest.fixture
def gauti_klientu_duomenis():
    return [1, 2, 3, 4, 5]

def test_fikstura(gauti_klientu_duomenis):
    assert len(gauti_klientu_duomenis) == 5


@pytest.fixture
def ploto_duomenys():
    ilgis = 5
    plotis = 10
    return ilgis, plotis


def test_apskaiciuoti_plota(ploto_duomenys):
    ilgis, plotis = ploto_duomenys
    assert fn.apskaiciuoti_plota(ilgis, plotis) == 50

@pytest.fixture
def mazo_ploto_duomenys():
    return 2,5

def test_apskaiciuoti_maza_plota(mazo_ploto_duomenys):
    ilgis, plotis = mazo_ploto_duomenys
    assert fn.apskaiciuoti_plota(ilgis, plotis) == 10

from unittest.mock import patch

@pytest.fixture
def mock_gauti_orus_response():
    return {'temperatura': 25, 'miestas': 'Vilnius'}

@patch('funkcijos.gauti_orus')
def test_apsirengti_siltai(mock_gauti_orus, mock_gauti_orus_response):
    mock_gauti_orus.return_value = mock_gauti_orus_response['temperatura']
    assert fn.apsirengti_siltai('Vilnius') == False

@pytest.fixture
def mock_gauti_zema_temperatura():
    return {'temperatura': 10}

@patch ('funkcijos.gauti_orus')
def test_apsirengti_siltai_tikrai(mock_gauti_orus, mock_gauti_zema_temperatura):
    mock_gauti_orus.return_value = mock_gauti_zema_temperatura['temperatura']
    assert fn.apsirengti_siltai('Kaunas') == True