# Password Manager

## ENGLISH
A simple command-line password manager written in Python.

The application allows users to securely store, manage, and retrieve passwords protected by a master password. All credentials are encrypted before being saved to disk using the Fernet symmetric encryption scheme from the `cryptography` library.

## Features

* Master password authentication
* Secure password storage with encryption
* Password generation using cryptographically secure randomness
* Add, modify, view, and delete credentials
* Clipboard support for quick password copying
* Local encrypted storage

## How It Works:

### 1) First Run

When the application is executed for the first time:

1. The user creates a master password.
2. A random salt is generated and stored in `salt.bin`.
3. A cryptographic key is derived from the master password using PBKDF2-HMAC-SHA256.
4. An encrypted password database (`password.enc`) is created.

### 2) Authentication

On subsequent executions:

1. The salt is loaded from `salt.bin`.
2. A key is derived from the entered master password.
3. The encrypted database is decrypted using the derived key.
4. If decryption succeeds, access is granted.

### 3) Data Storage

Passwords are stored as a list of records:

```
[
    {
        "Servizio": "Gmail",
        "Nome Utente": "user@example.com",
        "Password": "MyStrongPassword"
    }
]
```

The data is serialized to JSON, encrypted with Fernet, and saved inside `password.enc`.

### 4) Security

The project uses:

* PBKDF2-HMAC-SHA256 for key derivation
* 480,000 iterations
* Random 16-byt e salt
* Fernet authenticated encryption
* Cryptographically secure password generation via Python's `secrets` module

### 5) Requirements

Install dependencies:

```
pip install cryptography pyperclip
```

### 6) Usage

Run the application:

```
python main.py
```

Available operations:

1. Show Password
2. Add Password
3. Modify Password
4. Delete Password
5. Exit


## Modules

1) crypto_manager.py

Handles:

* Master password registration
* Authentication
* Key derivation
* Encryption and decryption

2) password_manager.py

Handles:

* Password management
* Password generation
* Clipboard operations
* Saving encrypted data

3) main.py

Provides the command-line user interface and coordinates the application workflow.

## Disclaimer

This project was developed for educational purposes and personal use. While it implements modern cryptographic primitives, it has not undergone a professional security audit and should not be considered a production-grade password manager.



# Gestore di password

## ITALIANO
Un semplice gestore di password a riga di comando scritto in Python.

L'applicazione consente agli utenti di archiviare, gestire e recuperare in modo sicuro le password protette da una password principale. Tutte le credenziali vengono crittografate prima di essere salvate su disco utilizzando lo schema di crittografia simmetrica Fernet della libreria `cryptography`.

## Funzionalità

* Autenticazione tramite password principale
* Archiviazione sicura delle password con crittografia
* Generazione di password tramite casualità crittograficamente sicura
* Aggiunta, modifica, visualizzazione ed eliminazione delle credenziali
* Supporto per gli appunti per copiare rapidamente le password
* Archiviazione locale crittografata

## Come funziona:

### 1) Prima esecuzione

Quando l'applicazione viene eseguita per la prima volta:

1. L'utente crea una password principale.
2. Viene generato un salt casuale e memorizzato in `salt.bin`.
3. Viene derivata una chiave crittografica dalla password principale utilizzando PBKDF2-HMAC-SHA256.
4. Viene creato un database di password crittografato (`password.enc`).

### 2) Autenticazione

Alle esecuzioni successive:

1. Il salt viene caricato da `salt.bin`.
2. Viene derivata una chiave dalla password principale inserita.
3. Il database crittografato viene decrittografato utilizzando la chiave derivata.
4. Se la decrittazione ha successo, l'accesso viene concesso.

### 3) Archiviazione dei dati

Le password vengono memorizzate come un elenco di record:

```
[
    {
        "Servizio": "Gmail",
        "Nome Utente": "user@example.com",
        "Password": "MyStrongPassword"
    }
]
```

I dati vengono serializzati in JSON, crittografati con Fernet e salvati all'interno di `password.enc`.


### 4) Sicurezza

Il progetto utilizza:

* PBKDF2-HMAC-SHA256 per la derivazione della chiave
* 480.000 iterazioni
* Salt casuale a 16 byte
* Crittografia autenticata con Fernet
* Generazione di password crittograficamente sicura tramite il modulo `secrets` di Python

### 5) Requisiti

Installa le dipendenze:

```
pip install cryptography pyperclip
```

### 6) Utilizzo

Esegui l'applicazione:

```
python main.py
```

Operazioni disponibili:

1. Mostra password
2. Aggiungi password
3. Modifica password
4. Elimina password
5. Esci

## Moduli

1) crypto_manager.py

Gestisce:

* Registrazione della password principale
* Autenticazione
* Derivazione della chiave
* Crittografia e decrittografia

2) password_manager.py

Gestisce:

* Password Gestione
* Generazione di password
* Operazioni negli appunti
* Salvataggio dei dati crittografati

3) main.py

Fornisce l'interfaccia utente a riga di comando e coordina il flusso di lavoro dell'applicazione.

## Avvertenza

Questo progetto è stato sviluppato a scopo didattico e per uso personale. Sebbene implementi primitive crittografiche moderne, non è stato sottoposto a una revisione di sicurezza professionale e non deve essere considerato un gestore di password di livello professionale.
