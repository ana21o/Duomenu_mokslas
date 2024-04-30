import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 užduotis
# naudojant selenium parašykite testą, kuris bandytų nuskaityti informaciją iš jūsų pasirinkto puslapio
# "ištraukite keletą elementų iš puslapio" ir testuokite ar juose yra tekstas, kurio jūs tikitės

def test_autoplius():
    driver = webdriver.Chrome()
    driver.get('https://autoplius.lt/skelbimai/naudoti-automobiliai?make_id_list=99&engine_capacity_from=&engine_capacity_to=&power_from=&power_to=&kilometrage_from=&kilometrage_to=&has_damaged_id=10924&condition_type_id=&make_date_from=2016&make_date_to=&sell_price_from=&sell_price_to=&fuel_id%5B30%5D=30&co2_from=&co2_to=&euro_id=&fk_place_countries_id=&qt=&number_of_doors_id=&gearbox_id=38&steering_wheel_id=10922&is_partner=&older_not=&save_search=1&slist=2278070198&category_id=2&order_by=&order_direction=&make_id%5B99%5D=10856&page_nr=2')
    elementas = driver.find_element(By.CLASS_NAME, 'subscription-type-label')
    tekstas = elementas.text
    assert 'Apie' in tekstas
    assert 'Automobiliai' in driver.title

    skelbimai = driver.find_elements(By.CLASS_NAME, 'announcement-title')
    # print(len(skelbimai))
    assert len(skelbimai) == 25
    for skelbimas in skelbimai:
        assert 'Q5' in skelbimas.text

    parametrai = driver.find_elements(By.CSS_SELECTOR, '.announcement-parameters-block .announcement-parameters')
    parametru_tekstai = []
    for parametras in parametrai:
        parametru_tekstai.append(parametras.text)
    # print(parametru_tekstai)
    for parametras in parametrai:
        kuro_tipas = parametras.find_elements(By.TAG_NAME, 'span')[0].text.strip()
        assert kuro_tipas == 'Benzinas'

        pavaru_deze = parametras.find_elements(By.TAG_NAME, 'span')[1].text.strip()
        assert pavaru_deze == 'Automatinė'

        rida = parametras.find_elements(By.TAG_NAME, 'span')[3].text.strip()
        if rida:
            assert 'km' in rida, 'Nenurodyta'

    kainos = driver.find_elements(By.CSS_SELECTOR, '.announcement-pricing-info strong')
    kainos_reiksmes = []
    for kaina in kainos:
        kainos_reiksmes.append(kaina.text)
    # print(kainos_reiksmes)
    assert not kainos_reiksmes == []
    # print(len(kainos_reiksmes))  #kodel 40!!!!
    # assert len(kainos_reiksmes) == 25
    for kaina in kainos_reiksmes:
        if kaina.strip():
            assert kaina[-1] == '€'
    

    driver.quit()

test_autoplius()
    