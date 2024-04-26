import smtplib

def send_email(sender, receiver, subject, body):
    smtp_server = 'gmail.com'
    smtp_port = 777

    with smtplib.SMTP() as server:
        server.sendmail(sender, receiver, subject, body)

def pranesti_vartotojui(email, ivykis):
    sender = 'antanas@gmail.com'
    subject = 'Tema'
    body = f'Sveiki, jus gavote email {ivykis}'
    send_email(sender, email, subject, body)   


def daugyba(num1, num2):
    return num1 * num2

def skaiciavimas(num1, num2):
    if num1 == num2:
        return num1 * num2
    return daugyba (num1 , num2)


# -------------------------------------

def nuskaityti_faila(failo_nuoroda):
    with open (failo_nuoroda, 'r') as failas:
        duomenys = failas.read()
        return duomenys
    
# print(nuskaityti_faila('tekstas.txt'))

def saraso_suma(sarasas):
    suma = 0
    for sk in sarasas:
        try:
            suma += sk
        except Exception as e:
            return 'klaida'
    return suma

def saraso_suma_2(sarasas):
    suma = 0
    for sk in sarasas:
        if not (isinstance(sk, int) or isinstance(sk, float)):
            raise Exception('Saraso nariai privalo buti skaiciai')
        suma += sk
    return suma

