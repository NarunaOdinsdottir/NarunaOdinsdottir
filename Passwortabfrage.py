def check_passwords(passwords, input_password):
    # Prüft, ob das eingegebene Passwort einem der erlaubten entspricht (case-insensitiv)
    return any(input_password.lower() == password.lower() for password in passwords)

# Begrüßung
print("Willkommen in Vault 83. Bitte geben Sie ein gültiges Passwort ein:")

# Passwortabfrage
eingabe = input("Passwort: ").strip()

# Liste gültiger Passwörter
passwords = [
    "The truth is, the game was rigged from the start.",
    "WastelandWonder",
    "Courier",
    "Dogmeat"
]

# Dictionary für Codes und Namen
codes = {
    "Bark": "Dusty",
    "Mutant": None,
    "Deathclaw": "Master",
    "Stimpak": "Kevin",
    "Master of Disaster": "Master Nane"
}

# Kein Passwort eingegeben?
if not eingabe:
    print("Stille? Ein getarnter Feind? Sicherheitsalarm!")
else:
    # Passwort korrekt?
    if check_passwords(passwords, eingabe):
        print("Passwort akzeptiert. Bitte geben Sie nun Ihren Identifikationscode ein.")
        
        versuche = 3
        while versuche > 0:
            id_code = input("Identifikationscode: ").strip()

            if id_code in codes:
                if id_code == "Mutant":
                    print("Zutritt verweigert. Gefechtsposten und Verteidigungsanlage aktiviert. Sie haben 39 Sekunden dieses Gebiet zu verlassen!")
                else:
                    name = codes[id_code]
                    print(f"Willkommen zurück {name}! Vault Tür wird geöffnet. Bitte zurücktreten.")
                break
            else:
                versuche -= 1
                if versuche > 0:
                    print(f"Falscher Code. Verbleibende Versuche: {versuche}")
                else:
                    print("Zu viele Fehlversuche. Selbstzerstörungsprotokoll aktiviert… 3… 2… 1… 💥")
    else:
        print("Zutritt verweigert! Das Passwort ist nicht korrekt.")