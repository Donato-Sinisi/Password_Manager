from password_manager import PasswordManager 
from crypto_manager import CryptoManager

CM = CryptoManager()
PM = None

def title():
    """Stampa il titolo del programma"""
    print("------------------------------")
    print("|      PASSWORD MANAGER      |")
    print("------------------------------")

def main():

    title()
    if CM.is_first_run():
        master_password = input("Crea la tua Master Password: ")
        CM.register_master_password(master_password)
    else:
        authenticated = False
        while not authenticated:
            master_password = input("Inserisci la Master Password: ")
            authenticated = CM.login(master_password)

    PM = PasswordManager(CM)
    PM.data = CM.decrypt_data()

    while True:
        title()
        action = input("Scegli l'azione che vuoi eseguire: " \
                        "\n1. Mostra Password" \
                        "\n2. Aggiungi Password" \
                        "\n3. Modifica Password" \
                        "\n4. Elimina Password " \
                        "\n5. Esci \n")
        match(action):
            case '1': 
                PM.show_password()
            case '2':
                PM.add_password()
            case '3':
                PM.modify_password()
            case '4':
                PM.delete_password()
            case '5':
                CM.logout()
                exit()

main()