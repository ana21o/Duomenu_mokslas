from ligonine import Ligonine

def main():

    ligonine = Ligonine()

    while True:
        print('\nPasirinkite veiksma:')
        print('1 - baigti darba')
        print('2 - prideti gydytoja')
        print('3 - prideti pacienta')
        print('4 - prideti susitikima')
        print('5 - perziureti duomenis')

        pasirinkimas = input('Iveskite pasirinkimo numeri: ')

        if pasirinkimas == '1':
            print('Programos pabaiga')
            break
        elif pasirinkimas == '2':
            print('Iveskite gydytojo informacija')
            vardas = input('Vardas: ')
            pavarde = input('Pavarde: ')
            specializacija = input('Specializacija: ')
            el_pastas = input('El_pastas: ')
            gydytojas = ligonine.prideti_gydytoja(vardas, pavarde, specializacija, el_pastas)
            print(f"gydytojas {gydytojas.vardas} buvo pridetas")
        elif pasirinkimas == '3':
            print('Iveskite paciento informacija')
            vardas = input('Vardas: ')
            pavarde = input('Pavarde: ')
            gimimo_data = input('Gimimo_data: ')
            lytis = input('Lytis: ')
            el_pastas = input('El_pastas: ')
            gydytojo_id = int(input('Gydytojo_id: '))
            pacientas = ligonine.prideti_pacienta(vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id)
            print(f"Pacientas {pacientas.vardas} buvo pridetas")
        elif pasirinkimas == "4":
            print("Iveskite susitikimo informacija")
            paciento_id = int(input("paciento_id: "))
            gydytojo_id = int(input("gydytojo_id: "))
            susitikimo_data = input("Susitikimo_data: ") 
            paskirtis = input("Paskirtis: ") 
            komentarai = input("Komentarai: ") 
            susitikimo_id = ligonine.prideti_susitikima(paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai)
            susitikimas = ligonine.gauti_susitikimo_info_pagal_id(susitikimo_id)
            pac_vardas , gyd_vardas, data = susitikimas
            print(f"Paciento {pac_vardas} susitikimas su gydytoju {gyd_vardas}  buvo pridetas. Vizito data: {data}")
        elif pasirinkimas == '5':
            lentele = input('Iveskite lenteles pavadinima: gydytojai/pacientai/susitikimai: ')
            while lentele not in ['gydytojai', 'pacientai', 'susitikimai']:
                lentele = input('Iveskite lenteles pavadinima: gydytojai/pacientai/susitikimai: ')
            ligonine.perziureti_irasus(lentele)

        else:
            print('Pasirinkimas neteisingas, bandykite dar karta')


if __name__ == '__main__':
    main()
