import string
import secrets
import pyperclip

class PasswordManager:
    """Contiene tutte le funzioni del Password Manager"""

    def __init__(self, crypto_manager):
        self.cm = crypto_manager
        self.data = []

    def save(self):
        encrypted = self.cm.encrypt_data(self.data)

        with open(self.cm.db_file, "wb") as file:
            file.write(encrypted)

    def add_password(self):
        """Permette di aggiungere una nuova password"""
        service = input("Inserisci il nome del servizio: ")
        user_name = input("Inserisci il nome utente: ")
        password = self.suggest_password()

        self.data.append(
            {
                "Servizio" : service,
                "Nome Utente" : user_name,
                "Password" : password
            }
        )
        self.save()

    def modify_password(self):
        """Permette di modificare una password esistente"""
        self.show_all_services_name()
        check_service = input("Inserisci il nome del servizio da modificare: ")
        for s in self.data:
            if s["Servizio"] == check_service:
                print(f"Servizio Trovato. Nome utente attuale: {s['Nome Utente']}")
                choice = input("Modificare il nome utente? (y/n): ")
                if choice == "y":
                    new_user_name = input(f"Inserisci il nuovo nome utente per {s['Servizio']}: ")
                    s['Nome Utente'] = new_user_name
                print(f"Inserisci la nuova password per {s['Servizio']} (password attuale: {s['Password']})")
                s['Password'] = self.suggest_password()
                self.save()
                return
       
        print("Servizio non trovato.")

    def show_all_services_name(self):
        """Mostra tutti i servizi salvati"""
        if not self.data:
            print("Non ci sono servizi salvati.")
            return False
        print("Password Salvate: ")
        for s in self.data:
            print(s['Servizio'])

        return True

    def show_password(self):
        """Mostra la password del servizio dato in input"""
        if self.show_all_services_name():
            show = input("Quale password vuoi visualizzare? ")
            for s in self.data:
                if show == s['Servizio']:
                    print(f"La password di {s['Servizio']} per l'utente {s['Nome Utente']} è {s['Password']}")
                    self.copy_password(s['Password'])
                    return
            
            print("Servizio non trovato.")
    
    def delete_password(self):
        """Permette di eliminare una password esistente"""
        self.show_all_services_name()
        delete = input("Quale password vuoi eliminare? ")
        for s in self.data:
            if delete == s['Servizio']:
                choice = input(f"Eliminare definitivamente la password di {s['Servizio']}? (y/n) ")
                if choice == "y":
                    self.data.remove(s)
                    self.save()
                    return

        print("Servizio non trovato.")

    def generate_password(self, length=15):
        """Genera una password forte di 15 caratteri"""
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = "".join(secrets.choice(characters) for _ in range(length))
        return generated_password
    
    def suggest_password(self):
        """Chiede all'utente se vuole generare o inserire una password"""
        choice = input("Vuoi generare automaticamente una password? (y/n) ")
        if choice == "y":
            password = self.generate_password()
            print(f"La password generata è {password}")
        else:
            password = input("Inserisci la password: ")
        return password

    def copy_password(self, password):
        """Copia la password negli appunti"""
        choice = input("Vuoi copiare la password negli appunti? (y/n) ")
        if choice == "y":
            pyperclip.copy(password)