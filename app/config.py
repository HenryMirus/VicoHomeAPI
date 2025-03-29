import os
from dotenv import load_dotenv

# .env-Datei laden
load_dotenv()

# Werte aus der .env-Datei abrufen
API_KEY = os.getenv("API_KEY")
CAMERA_ID = os.getenv("CAMERA_ID")
SAVE_DIRECTORY = os.getenv("SAVE_DIRECTORY")

# Optional: Überprüfen, ob die Variablen korrekt geladen wurden
if not all([API_KEY, CAMERA_ID, SAVE_DIRECTORY]):
    raise ValueError("Eine oder mehrere Umgebungsvariablen fehlen!")