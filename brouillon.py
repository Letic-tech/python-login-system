import random
secret = random.randint(1, 10)
joueur = 0
n = 0

while joueur != secret:
    joueur = int(input("entrez votre nombre: "))
    n = n + 1
    if joueur > secret:
        print("Trop loin du chiffre")
    elif joueur < secret:
        print("trop en dessous du chiffre")
    else:
        print("Brava!")
print("Tu as trouve en", n , "essais")

def addition(a,b):
    return a * b

resultat = addition(4,5)
print(resultat)

import random

def demander_nombre():
    return int(input("Entrez un nombre: "))

def verifier(joueur, secret):
    if joueur > secret:
        print("trop grand")
    elif joueur < secret:
        print("trop petit")
    else:
        print("Bravissime!")


def jeu ():
    secret = random.randint(1, 10)
    tentatives = 0
    max_tentatives = 5
    joueur = 0

    while joueur != secret and tentatives < max_tentatives:
        print("Il vous reste ",max_tentatives - tentatives," tentatives")
        joueur = demander_nombre()
        tentatives = tentatives + 1
        verifier(joueur, secret)

    if joueur == secret:
        print("Tu as trouve en ", tentatives ," essais")
    else:
        print("Perdu le nombre etait: ", secret)
jeu()


import random

def spieler_Nummer():
    return int(input("Geben sie Ihre Zahl an: "))

def verifizierung(spieler,geheimnis):

    if spieler < geheimnis:
        print("Zu klein ")
    elif spieler > geheimnis:
        print("Zu gross")
    else:
        print("Super! Sie haben gefunden")

def stufe():
    anwort = input("Mochten Sie nochmal spielen? (j/n oder ja/nein) : ").lower().strip()
    if anwort in ("ja", "j"):
        return(spiel())
    elif anwort in ("nein","n"):
        print("Danke!")
    else:
        print("Invalid AnWort")


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

def main():
    while True:
        spiel()

        antwort = input("Möchten Sie nochmal spielen? (j/n): ").lower().strip()
        if antwort not in ("j", "ja"):
            print("Danke fürs Spielen!")
            break

main()

def login():
    nom = input("Geben Sie Ihren Namen: ")
    passwort = input("Geben Sie Ihren passwort: ")
    return nom, passwort



       if name == "admin" and passwort == "1234":
            print("Anmeldung erfolgreich!")

            import os

def registrierung():

        saved_username = input("Neuer Benutzername: ")
        saved_passwort = input("Neues Passwort: ")
        with open("user.txt", "a") as f:
        f.write(saved_username + "," + saved_passwort + "\n")

    print("Registrierung abgeschlossen\n")   
    return saved_username, saved_passwort


def login():
    username, passwort = registrierung()

    versuche = 0
    max_versuche = 3
    
    username = input("Geben Sie Ihren Namen: ")
    passwort = input("Geben Sie Ihren passwort: ")

    while versuche < max_versuche:
        with open("user.txt", "r") as f:
            for line in f:
            saved_username, saved_passwort = line.strip().split(",")


            if not os.path.exists("user.txt"):
                print("Kein Benutzer gefunden. Registrierung nötig.")
                registrierung()
                break
            if username == saved_username and passwort == saved_passwort :
                print("Login erfolgreich")
                break
            else:
                 print("Flasch, bitte nochmal versuchen")
        versuche = versuche + 1             

    if versuche == max_versuche:
        print("Konto gesperrt")
        print(saved_username,", Sie haben schon 3 Versuchen gemacht")

login()





   