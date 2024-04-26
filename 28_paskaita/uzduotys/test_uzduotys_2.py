import pytest
from uzduotys_2 import patvirtinti_apmokejima, patvirtinti_apmokejima_ar_yra
from unittest.mock import patch, mock_open


# 1

def test_patvirtinti_apmokejima():
    assert patvirtinti_apmokejima('LT5555', 250) == True
    assert patvirtinti_apmokejima('LT5555', 400) == False

@pytest.fixture
def mock_patvirtinti_apmokejima_atsakymas():
    return True

@patch('uzduotys_2.patvirtinti_apmokejima')
def test_patvirtinti_apmokejima_ar_yra(mock_patvirtinti_apmokejima, mock_patvirtinti_apmokejima_atsakymas):
    mock_patvirtinti_apmokejima.return_value = True
    mock_patvirtinti_apmokejima.return_value = mock_patvirtinti_apmokejima_atsakymas
    assert patvirtinti_apmokejima_ar_yra('LT6666', 2654) == "Banko sąskaita LT6666 gali atlikti mokėjimą"

@patch('uzduotys_2.patvirtinti_apmokejima')
def test_patvirtinti_apmokejima_ar_nera(mock_patvirtinti_apmokejima, mock_patvirtinti_apmokejima_atsakymas):
    mock_patvirtinti_apmokejima.return_value = False
    assert patvirtinti_apmokejima_ar_yra('LT6666', 2659) == "Banko sąskaita LT6666 negali atlikti mokėjimą"

@patch ('uzduotys_2.patvirtinti_apmokejima')
def test_patikrinti_saskaitos_nr(mock_patvirtinti_apmokejima, mock_patvirtinti_apmokejima_atsakymas):
    mock_patvirtinti_apmokejima.return_value = True
    assert patvirtinti_apmokejima_ar_yra('LT7777', 954876) == "Banko sąskaita LT7777 gali atlikti mokėjimą"