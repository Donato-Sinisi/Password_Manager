import os
import json
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

class CryptoManager:
    """Gestisce accesso e crittografia del file contenente le password"""

    def __init__(self):
        self.salt_file = "salt.bin"
        self.db_file = "password.enc"
        self.current_key = None

    def is_first_run(self):
        """Controlla se il codice viene eseguito per la prima volta"""
        return not os.path.exists(self.salt_file)

    def register_master_password(self, password):
        """Configura la master password una volta e genera il salt"""
        salt = os.urandom(16)
        with open(self.salt_file, "wb") as file:
            file.write(salt)

        self.current_key = self.derive_key(password, salt)

        f = Fernet(self.current_key)
        encrypted_data = f.encrypt(b"[]")
        with open(self.db_file, "wb") as file:
            file.write(encrypted_data)

        print("Registrazione completata con successo!")

    def login(self, password):
        """Tenta l'accesso leggendo il salt e verificando la password"""
        if self.is_first_run():
            print("Nessuna master password registrata.")
            return False
        
        with open(self.salt_file, "rb") as file:
            salt = file.read()

        potential_key = self.derive_key(password, salt)

        try:
            with open(self.db_file, "rb") as file:
                encrypted_data = file.read()

                f = Fernet(potential_key)
                f.decrypt(encrypted_data)

                self.current_key = potential_key
                print("Accesso autorizzato.")
                return True
        except Exception:
            print("Accesso negato")
            return False

    def logout(self):
        """Cancella la chiave dalla memoria bloccando la sessione"""
        self.current_key = None
        print("Sessione terminata con successo.")
        return

    def derive_key(self, password, salt):
        """Deriva una chiave fernet dalla password che immette l'utente"""
    
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        
        key = base64.urlsafe_b64encode(
            kdf.derive(password.encode())
        )
        return key
    
    def encrypt_data(self, data):
        """Serializza in json e cifra i dati"""
        f = Fernet(self.current_key)
        json_data = json.dumps(data).encode()
        return f.encrypt(json_data)
    
    def decrypt_data(self):
        """Serializza in json e decifra i dati"""
        f = Fernet(self.current_key)

        if not os.path.exists(self.db_file):
            return []
        
        with open(self.db_file, "rb") as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)
        data = json.loads(decrypted.decode())

        if isinstance(data, dict):
            return []
        
        return data