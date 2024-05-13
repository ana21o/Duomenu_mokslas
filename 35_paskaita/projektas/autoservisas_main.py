from autoservisas import Autoservisas

def main():

    autoservisas = Autoservisas()

    while True:
        print('\nPasirinkite veiksma:')
        print('1 - baigti darba')
        print('2 - prideti mechanika')
        print('3 - prideti klienta')
        print('4 - prideti automobili') 
        print('5 - prideti remonta')
        print('6 - perziureti duomenis')
        print('7 - peržiūrėti, kiek klientas sumokėjo už visų savo automobilių visus remontus')


        pasirinkimas = input('Iveskite pasirinkimo numeri: ')

        if pasirinkimas == '1':
            print('Programos pabaiga')
            break
        elif pasirinkimas == '2':
            print('Iveskite mechaniko informacija')
            vardas = input('Vardas: ')
            pavarde = input('Pavarde: ')
            el_pastas = input('el_pastas: ')
            valandinis_atlyginimas = float(input('Valandinis atlyginimas: '))
            specializacija = input('Specializacija: ')
            mechanikas = autoservisas.prideti_mechanika(vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija)
            print(f"Mechanikas {mechanikas.vardas} buvo pridetas")
        elif pasirinkimas == '3':
            print('Iveskite kliento informacija')
            vardas = input('Vardas: ')
            pavarde = input('Pavarde: ')
            el_pastas = input('el_pastas: ')
            mechaniko_id = int(input('Mechaniko_id: '))
            klientas = autoservisas.prideti_klienta(vardas, pavarde, el_pastas, mechaniko_id)
            print(f"Klientas {klientas.vardas} buvo pridetas")
        elif pasirinkimas == '4':
            print('Iveskite automobilio informacija')
            valstybinis_numeris = input('Valstybinis numeris: ')
            marke = input('Marke: ')
            modelis = input('Modelis: ')
            kliento_id = int(input('Kliento_id: '))
            automobilis = autoservisas.prideti_automobili(valstybinis_numeris, marke, modelis, kliento_id)
            print(f"Automobilis {automobilis.marke} {automobilis.modelis} buvo pridetas")
        elif pasirinkimas == '5':
            print('Iveskite remonto informacija')
            kliento_id = int(input('Kliento id: '))
            mechaniko_id = int(input('Mechaniko id: '))
            darbo_pradzia = input('Darbo pradzios laikas (YYYY-MM-DD HH:MM:SS): ')
            darbo_pabaiga = input('Darbo pabaigos laikas (YYYY-MM-DD HH:MM:SS): ')
            # uzimtas laikas ar laisvas
            remonto_kategorija = input('Remonto kategorija: ')
            if autoservisas.ar_laisvas_mechanikas(darbo_pradzia, darbo_pabaiga, kliento_id):
                remontas = autoservisas.prideti_remonta(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, remonto_kategorija)
                print(f"Remontas {remontas.remonto_kategorija} buvo pridetas")
            else:
                print("Atsiprašome, bet šiuo metu nėra laisvų mechanikų. Prašome palaukti.")
        elif pasirinkimas == '6':
            lentele = input('Iveskite lenteles pavadinima: mechanikai/klientai/automobiliai/remontas: ')
            while lentele not in ['mechanikai', 'klientai', 'automobiliai', 'remontas']:
                lentele = input('Iveskite lenteles pavadinima: mechanikai/klientai/automobiliai/remontas: ')
            autoservisas.perziureti_irasus(lentele)

        else:
            print('Pasirinkimas neteisingas, bandykite dar karta')

if __name__ == '__main__':
    main()