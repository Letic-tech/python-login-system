# 1. Basis-Image festlegen
FROM python:3.12

# 2. Arbeitsverzeichnis im Container erstellen
WORKDIR /app

# 3. requirements.txt kopieren und Flask/Werkzeug installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Alle Dateien aus unserem Projekt in den Container kopieren
COPY . .

# 5. Port 5000 nach außen freigeben
EXPOSE 5000

# 6. Den Befehl ausführen (deine Hauptdatei im Projekt)
CMD ["python", "app/app.py"]