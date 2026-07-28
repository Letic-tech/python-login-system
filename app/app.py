import os
import random
from flask import Flask, redirect, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
#  Secret Key für die Session-Verschlüsselung
app.secret_key = "mein_geheimer_schluessel_123"

# LOGIN SEITE 
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("stufe"))

    return '''
    <html>
    <head>
        <title>Willkommen</title>
        <style>
            body { font-family: Arial; background: #e3f2fd; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .box { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.2); text-align: center; width: 300px; }
            input { margin: 10px 0; padding: 10px; width: 90%; border-radius: 5px; border: 1px solid #ccc; }
            button { padding: 10px 20px; background: #2196F3; color: white; border: none; border-radius: 5px; cursor: pointer; width: 100%; margin-top: 10px; }
            button:hover { background: #1976D2; }
            a { color: #2196F3; text-decoration: none; font-size: 14px; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Login</h2>
            <form method="POST" action="/login">
                <input type="text" name="username" placeholder="Benutzername" required><br>
                <input type="password" name="password" placeholder="Passwort" required><br>
                <button type="submit">Login</button>
            </form>
            <br>
            <a href="/register">Noch kein Konto? Registrieren</a>
        </div>
    </body>
    </html>
    '''

# REGISTRIERUNG SEITE
@app.route("/register")
def register_page():
    return '''
    <html>
    <head>
        <title>Registrierung</title>
        <style>
            body { font-family: Arial; background: #f2f2f2; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .box { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.2); text-align: center; width: 300px; }
            input { margin: 10px 0; padding: 10px; width: 90%; border-radius: 5px; border: 1px solid #ccc; }
            button { padding: 10px 20px; background: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer; width: 100%; margin-top: 10px; }
            button:hover { background: #45a049; }
            a { color: #4CAF50; text-decoration: none; font-size: 14px; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Registrierung</h2>
            <form method="POST" action="/register">
                <input type="text" name="username" placeholder="Benutzername" required><br>
                <input type="password" name="password" placeholder="Passwort" required><br>
                <button type="submit">Registrieren</button>
            </form>
            <br>
            <a href="/">Zurück zum Login</a>
        </div>
    </body>
    </html>
    '''

# REGISTRIERUNG LOGIK
@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    hashed_password = generate_password_hash(password)

    os.makedirs("data", exist_ok=True)

    if os.path.exists("data/user.txt"):
        with open("data/user.txt", "r") as f:
            for line in f:
                if not line.strip():
                    continue
                existing_username, _ = line.strip().split(",", maxsplit=1)
                if username == existing_username:
                    return "Benutzer existiert bereits! <a href='/register'>Nochmal versuchen</a>"

    with open("data/user.txt", "a") as f:
        f.write(username + "," + hashed_password + "\n")

    return "Registrierung abgeschlossen! <a href='/'>Jetzt einloggen</a>"

# LOGIN LOGIK
@app.route("/login", methods=["POST"])
def login():
    if not os.path.exists("data/user.txt"):
        return "Kein Benutzer gefunden. <a href='/register'>Bitte registrieren</a>."

    # Input-Daten säubern (strippen entfernt versehentliche Leerzeichen)
    username = request.form["username"].strip()
    password = request.form["password"].strip()

    with open("data/user.txt", "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue

            # Teilt die Zeile NUR beim allerersten Komma auf!
            if "," in clean_line:
                saved_username, saved_password = clean_line.split(",", 1)
                saved_username = saved_username.strip()
                saved_password = saved_password.strip()

                # Prüfen ob Benutzername passt
                if username == saved_username:
                    # Prüfen ob Passwort-Hash übereinstimmt
                    if check_password_hash(saved_password, password):
                        session["username"] = username
                        return redirect(url_for("stufe"))
                    else:
                        print(f"DEBUG: Passwort für '{username}' war falsch!")

    return "Falscher Benutzername oder Passwort! <a href='/'>Nochmal versuchen</a>"


# STUFEN-AUSWAHL 
@app.route("/stufe")
def stufe():
    if "username" not in session:
        return redirect(url_for("home"))

    return '''
    <html>
    <head>
        <title>Stufe wählen</title>
        <style>
            body { font-family: Arial; background: #e0f2f1; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: white; padding: 40px; border-radius: 12px; text-align: center; width: 350px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
            h2 { color: #00695c; }
            a.btn { display: block; padding: 12px; margin: 10px 0; background: #00897b; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; }
            a.btn:hover { background: #00695c; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Welche Stufe? </h2>
            <a href="/start_game/einfach" class="btn">Einfach (Zahl 1-10, 5 Versuche)</a>
            <a href="/start_game/mittel" class="btn">Mittel (Zahl 1-20, 5 Versuche)</a>
            <a href="/start_game/schwer" class="btn">Schwer (Zahl 1-30, 4 Versuche)</a>
        </div>
    </body>
    </html>
    '''

# SPIEL INITIALISIEREN
@app.route("/start_game/<wahl>")
def start_game(wahl):
    if "username" not in session:
        return redirect(url_for("home"))

    # Logik stufe()-Funktion:
    if wahl == "einfach":
        max_nummer, max_versuche = 10, 5
    elif wahl == "schwer":
        max_nummer, max_versuche = 30, 4
    else:  # mittel
        max_nummer, max_versuche = 20, 5

    # Geheimnis und Versuche in der Session speichern
    session["geheimnis"] = random.randint(1, max_nummer)
    session["max_versuche"] = max_versuche
    session["max_nummer"] = max_nummer
    session["versuche"] = 0
    session["feedback"] = f"Errate die Zahl zwischen 1 und {max_nummer}!"
    session["game_over"] = False

    return redirect(url_for("game"))


#  DAS SPIEL (verifizierung()-Logik & Formular) ---
@app.route("/game", methods=["GET", "POST"])
def game():
    if "username" not in session:
        return redirect(url_for("home"))

    if "geheimnis" not in session:
        return redirect(url_for("stufe"))

    if request.method == "POST":
        if not session.get("game_over", False):
            try:
                spieler = int(request.form.get("spieler", 0))
                session["versuche"] += 1
                verblieben = session["max_versuche"] - session["versuche"]
                geheimnis = session["geheimnis"]

                # Deine verifizierung()-Logik:
                if spieler < geheimnis:
                    session["feedback"] = f"Zu klein! (Noch {verblieben} Versuch(e))"
                elif spieler > geheimnis:
                    session["feedback"] = f"Zu groß! (Noch {verblieben} Versuch(e))"
                else:
                    session["feedback"] = f" Super! Sie haben die Zahl in {session['versuche']} Versuchen gefunden!"
                    session["game_over"] = True

                # Prüfen ob verloren:
                if session["versuche"] >= session["max_versuche"] and not session["game_over"]:
                    session["feedback"] = f"Sie haben verloren. Die Nummer war {geheimnis}."
                    session["game_over"] = True

            except ValueError:
                session["feedback"] = "Bitte eine gültige Zahl eingeben!"

    # Formular nur anzeigen, wenn das Spiel noch läuft
    eingabe_html = '''
        <form method="POST" action="/game">
            <input type="number" name="spieler" placeholder="Deine Zahl" required autofocus><br>
            <button type="submit">Raten</button>
        </form>
    ''' if not session.get("game_over") else ''

    return f'''
    <html>
    <head>
        <title>Zahlen-Raten</title>
        <style>
            body {{ font-family: Arial; background: #e0f2f1; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .card {{ background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; width: 350px; }}
            h2 {{ color: #00695c; }}
            p {{ font-size: 16px; color: #333; }}
            input {{ margin: 10px 0; padding: 10px; width: 80%; border-radius: 5px; border: 1px solid #ccc; text-align: center; font-size: 16px; }}
            button {{ padding: 10px 20px; background: #00897b; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; margin-top: 10px; }}
            button:hover {{ background: #00695c; }}
            .btn-link {{ color: #00897b; text-decoration: none; font-size: 14px; display: inline-block; margin-top: 15px; }}
            .logout-btn {{ color: #e53935; text-decoration: none; font-size: 14px; display: block; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Spieler: {session['username']} </h2>
            <p><b>{session.get('feedback', '')}</b></p>
            
            {eingabe_html}

            <br>
            <a href="/stufe" class="btn-link"> Andere Stufe wählen</a>
            <a href="/logout" class="logout-btn">Abmelden (Logout)</a>
        </div>
    </body>
    </html>
    '''

# --- LOGOUT ---
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)