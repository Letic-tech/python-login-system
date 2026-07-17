import random
import os
import sys


def menu():

    """
    print ("Bitte wahlen Sie eine Option 1, 2 oder 3")
    Registrieren = int(input("1 - Registration: "))
    Login = int(input("2 - Login: "))
    Beenden = int(input("3 - Beenden: "))
    """
    
    while True:

        print("1 - Registration")
        print("2 - Login")
        print("3 - Beenden")

        Wahl = input("wahl: ")
        
        if Wahl == "1":
            registrierung()
            
        elif Wahl == "2":
            Login()
            
        elif Wahl == "3":
            beenden()
        else:
            print("Ungültige Wahl, bitte versuchen Sie es erneut.\n")

           

def registrierung():
    print("REGISTRATION")
    saved_username = input("Neuer Benutzername: ")

    if os.path.exists("user.txt"):
        with open("user.txt", "r") as f:
            for line in f:
                if not line.strip():
                    continue
                existing_username, _ = line.strip().split(",", maxsplit=1)
                if saved_username == existing_username:
                    print("Sie sind schon angemeldet! (Ce nom est déjà pris)")
                    return

    saved_passwort = input("Neuer Passwort: ")
    with open("user.txt", "a") as f:
        f.write(saved_username + "," + saved_passwort + "\n")
        print("Registrierung abgeschlossen\n")

def Login():
    if not os.path.exists("user.txt"):
        print("kein benutzer gefunden. Registrierung notig.")
        registrierung()
        return
    versuche = 0
    max_versuche = 3

    while versuche < max_versuche:
        print("Willkommen konnen Sie sich loggen?")
        username = input("Benutzername:")
        passwort = input ("Passwort: ")
        gefunden = False

        with open("user.txt", "r") as f:
            for line in f:
                saved_username, saved_passwort = line.strip().split(",", maxsplit=1)


                if username == saved_username and passwort == saved_passwort:
                    print("Login erfolgreich !")
                    gefunden = True
                    break

                
        if gefunden:
            spiel()
            return
        else:
            print("Falsch, bitte nochmal versuchen")
            versuche += 1

    print ("Konto gesperrt")


def beenden():
    print("Danke fur dein Spielen. Bis Bald!")
    sys.exit()



def spieler_Nummer():
    return int(input("Geben sie Ihre Zahl an: "))

def verifizierung(spieler,geheimnis):

    if spieler < geheimnis:
        print("Zu klein ")
    elif spieler > geheimnis:
        print("Zu gross")
    else:
        print("Super! Sie haben gefunden")
"""
def stufe():
    anwort = input("Mochten Sie nochmal spielen? (j/n oder ja/nein) : ").lower().strip()
    if anwort in ("ja", "j"):
        return(spiel())
    elif anwort in ("nein","n"):
        print("Danke!")
    else:
        print("Invalid AnWort")
"""

def stufe():
    while True:
        wahl = input("Welche Stufe? (einfach/mittel/schwer): ").lower().strip()

        if wahl == "einfach":
            return 10, 5
        elif wahl == "mittel":
            return 20, 5
        elif wahl == "schwer":
            return 30, 4
        else:
            print("Ungültige Wahl. Bitte erneut versuchen.")

def spiel():
    max_nummer, max_versuche = stufe()
    geheimnis = random.randint(1,max_nummer)
    spieler = 0
    versuche = 0
  

    while spieler != geheimnis and versuche < max_versuche:
        print("Sie haben noch ", max_versuche - versuche ,"Versuche")

        spieler = spieler_Nummer()
        versuche = versuche + 1
        verifizierung(spieler,geheimnis)

    if spieler == geheimnis:
            print("Sie haben in ", versuche,"Versuchen gefunden")
    else:
            print("Sie haben verloren. Die nummer war ", geheimnis)

menu()
